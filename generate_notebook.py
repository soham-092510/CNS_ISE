import json
import os

notebook_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Group5_RandomForest_Phishing.ipynb")

cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# CNS ISE - Group 5 Research Framework\n",
            "## Heuristic URL Feature Profiling for Phishing Domain Spotting Using Hyper-Tuned Random Forest Ensembles\n",
            "\n",
            "**Author:** Group 5  \n",
            "**Target Framework:** IEEE Layout Style  \n",
            "**Dataset:** Kaggle Phishing Website Detector (30 Heuristic URL Features)  \n",
            "\n",
            "### Assigned Group 5 Mechanics:\n",
            "1. Implement `sklearn.ensemble.RandomForestClassifier`.\n",
            "2. Execute broad hyperparameter sweeps across tree bounds ($n_{\\text{estimators}}$ scaling 50 to 200, $\\text{max\\_depth}$ ranges).\n",
            "3. Generate Out-of-Bag (OOB) error decline tracking plots.\n",
            "4. Extract Mean Decrease in Gini Impurity (MDI) matrices to rank diagnostic structural weights of the 30 URL features.\n",
            "5. Benchmark computational overhead and inference latency for Group 1 (Section 5.2).\n",
            "6. Generate evaluation tournament leaderboard metrics for Group 3 (Section 5.1).\n",
            "7. Author Sections 1, 2, 3.5, and 6 of the academic paper."
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Step 1: Import Dependencies & System Environment Verification\n",
            "Here we initialize all required scientific libraries and capture system runtime information for Group 4 (Section 4)."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "import os\n",
            "import sys\n",
            "import time\n",
            "import platform\n",
            "import glob\n",
            "import numpy as np\n",
            "import pandas as pd\n",
            "import matplotlib.pyplot as plt\n",
            "import sklearn\n",
            "from sklearn.model_selection import train_test_split, GridSearchCV\n",
            "from sklearn.ensemble import RandomForestClassifier\n",
            "from sklearn.metrics import (\n",
            "    accuracy_score, precision_score, recall_score, f1_score,\n",
            "    roc_auc_score, roc_curve, confusion_matrix, ConfusionMatrixDisplay,\n",
            "    classification_report\n",
            ")\n",
            "\n",
            "# Ensure output directories exist\n",
            "for d in [\"data\", \"figures\", \"results\", \"results/handovers\"]:\n",
            "    os.makedirs(d, exist_ok=True)\n",
            "\n",
            "print(f\"[System Specs] OS: {platform.system()} {platform.release()}\")\n",
            "print(f\"[System Specs] Python: {sys.version.split()[0]}\")\n",
            "print(f\"[System Specs] Scikit-Learn: {sklearn.__version__}\")\n",
            "print(f\"[System Specs] Pandas: {pd.__version__}\")\n",
            "print(f\"[System Specs] NumPy: {np.__version__}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Step 2: Intelligent Dataset Ingestion\n",
            "The notebook checks the `data/` folder for any downloaded Kaggle CSV (`phishing.csv`, `dataset.csv`, etc.).\n",
            "If you haven't downloaded it yet, a starter 30-feature dataset is automatically prepared so the pipeline runs smoothly."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "UCI_30_FEATURES = [\n",
            "    \"having_IP_Address\", \"URL_Length\", \"Shortining_Service\", \"having_At_Symbol\",\n",
            "    \"double_slash_redirecting\", \"Prefix_Suffix\", \"having_Sub_Domain\", \"SSLfinal_State\",\n",
            "    \"Domain_registeration_length\", \"Favicon\", \"port\", \"HTTPS_token\",\n",
            "    \"Request_URL\", \"URL_of_Anchor\", \"Links_in_tags\", \"SFH\",\n",
            "    \"Submitting_to_email\", \"Abnormal_URL\", \"Redirect\", \"on_mouseover\",\n",
            "    \"RightClick\", \"popUpWidnow\", \"Iframe\", \"age_of_domain\",\n",
            "    \"DNSRecord\", \"web_traffic\", \"Page_Rank\", \"Google_Index\",\n",
            "    \"Links_pointing_to_page\", \"Statistical_report\"\n",
            "]\n",
            "\n",
            "# Locate dataset\n",
            "csv_candidates = glob.glob(\"data/*.csv\")\n",
            "user_csvs = [f for f in csv_candidates if \"sample\" not in os.path.basename(f).lower()]\n",
            "\n",
            "if user_csvs:\n",
            "    dataset_path = user_csvs[0]\n",
            "    print(f\"[SUCCESS] Loaded User Kaggle Dataset: {dataset_path}\")\n",
            "    df = pd.read_csv(dataset_path)\n",
            "elif csv_candidates:\n",
            "    dataset_path = csv_candidates[0]\n",
            "    print(f\"[INFO] Loaded Dataset: {dataset_path}\")\n",
            "    df = pd.read_csv(dataset_path)\n",
            "else:\n",
            "    # Fallback generator if user hasn't copied the Kaggle CSV yet\n",
            "    print(\"[INFO] Generating sample dataset with 30 heuristic features...\")\n",
            "    np.random.seed(42)\n",
            "    sample_data = {feat: np.random.choice([-1, 0, 1], size=1500, p=[0.45, 0.1, 0.45]) for feat in UCI_30_FEATURES}\n",
            "    score = (sample_data[\"SSLfinal_State\"] * 2.5 + sample_data[\"URL_of_Anchor\"] * 2.2 + \n",
            "             sample_data[\"having_Sub_Domain\"] * 1.8 + sample_data[\"having_IP_Address\"] * 1.5 + np.random.normal(0, 1, 1500))\n",
            "    sample_data[\"Result\"] = np.where(score > 0, 1, -1)\n",
            "    df = pd.DataFrame(sample_data)\n",
            "    df.to_csv(\"data/phishing_sample.csv\", index=False)\n",
            "    print(\"[SUCCESS] Created 'data/phishing_sample.csv'. (Replace with Kaggle CSV when ready!)\")\n",
            "\n",
            "df.head()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Step 3: Dataset Preprocessing & Schema Verification\n",
            "Verify missing values, normalize ID columns, and map target labels: `-1 -> 0 (Phishing)` and `1 -> 1 (Legitimate)`."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Drop potential ID columns\n",
            "id_cols = [c for c in df.columns if c.lower() in [\"id\", \"index\", \"unnamed: 0\"]]\n",
            "if id_cols:\n",
            "    df = df.drop(columns=id_cols)\n",
            "\n",
            "# Identify target column\n",
            "target_candidates = [\"result\", \"class_label\", \"target\", \"label\", \"class\"]\n",
            "target_col = next((c for c in df.columns if c.strip().lower() in target_candidates), df.columns[-1])\n",
            "print(f\"Target column identified: '{target_col}'\")\n",
            "\n",
            "X = df.drop(columns=[target_col])\n",
            "y_raw = df[target_col]\n",
            "\n",
            "if set(y_raw.unique()) == {-1, 1}:\n",
            "    y = y_raw.map({-1: 0, 1: 1})\n",
            "    print(\"Mapped target values: {-1: 0 (Phishing), 1: 1 (Legitimate)}\")\n",
            "else:\n",
            "    y = y_raw\n",
            "\n",
            "print(f\"Feature matrix shape: {X.shape}\")\n",
            "print(f\"Total Features: {X.shape[1]}\")\n",
            "print(f\"Missing values in dataset: {df.isnull().sum().sum()}\")\n",
            "print(f\"Class Distribution:\\n{y.value_counts()}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Step 4: Stratified Train-Test Partitioning\n",
            "We partition the dataset into 80% training and 20% testing subsets with fixed random state 42 for reproducible benchmarking."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "X_train, X_test, y_train, y_test = train_test_split(\n",
            "    X, y, test_size=0.20, random_state=42, stratify=y\n",
            ")\n",
            "print(f\"Training instances: {X_train.shape[0]}\")\n",
            "print(f\"Testing instances:  {X_test.shape[0]}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Step 5: Baseline Random Forest Classifier\n",
            "Establish baseline classification metrics with default $n_{\\text{estimators}}=100$."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "baseline_rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)\n",
            "baseline_rf.fit(X_train, y_train)\n",
            "y_pred_base = baseline_rf.predict(X_test)\n",
            "\n",
            "print(\"=== Baseline Random Forest Metrics ===\")\n",
            "print(f\"Accuracy : {accuracy_score(y_test, y_pred_base)*100:.2f}%\")\n",
            "print(f\"Precision: {precision_score(y_test, y_pred_base)*100:.2f}%\")\n",
            "print(f\"Recall   : {recall_score(y_test, y_pred_base)*100:.2f}%\")\n",
            "print(f\"F1-Score : {f1_score(y_test, y_pred_base)*100:.2f}%\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Step 6: Broad Hyperparameter Sweeps\n",
            "1. Tree bounds ($n_{\\text{estimators}}$ scaling from 50 to 200).\n",
            "2. Maximum tree depth ranges ($[5, 10, 15, 20, 25, 30, \\text{None}]$)."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Sweep n_estimators\n",
            "tree_counts = [50, 75, 100, 125, 150, 175, 200]\n",
            "acc_trees = []\n",
            "for n in tree_counts:\n",
            "    rf = RandomForestClassifier(n_estimators=n, random_state=42, n_jobs=-1)\n",
            "    rf.fit(X_train, y_train)\n",
            "    acc_trees.append(accuracy_score(y_test, rf.predict(X_test)))\n",
            "\n",
            "plt.figure(figsize=(7, 4))\n",
            "plt.plot(tree_counts, acc_trees, marker='o', color='#1f77b4', lw=2)\n",
            "plt.title(\"Random Forest Accuracy vs. Number of Estimators\", fontweight='bold')\n",
            "plt.xlabel(\"Number of Estimators (n_estimators)\")\n",
            "plt.ylabel(\"Test Accuracy\")\n",
            "plt.grid(True, linestyle='--', alpha=0.6)\n",
            "plt.tight_layout()\n",
            "plt.savefig(\"figures/rf_accuracy_vs_trees.png\", dpi=300)\n",
            "plt.show()\n",
            "\n",
            "# Sweep max_depth\n",
            "depth_values = [5, 10, 15, 20, 25, 30, None]\n",
            "acc_depths = []\n",
            "for d in depth_values:\n",
            "    rf = RandomForestClassifier(n_estimators=100, max_depth=d, random_state=42, n_jobs=-1)\n",
            "    rf.fit(X_train, y_train)\n",
            "    acc_depths.append(accuracy_score(y_test, rf.predict(X_test)))\n",
            "\n",
            "plt.figure(figsize=(7, 4))\n",
            "plt.plot([str(d) for d in depth_values], acc_depths, marker='s', color='#2ca02c', lw=2)\n",
            "plt.title(\"Random Forest Accuracy vs. Maximum Tree Depth\", fontweight='bold')\n",
            "plt.xlabel(\"Maximum Depth (max_depth)\")\n",
            "plt.ylabel(\"Test Accuracy\")\n",
            "plt.grid(True, linestyle='--', alpha=0.6)\n",
            "plt.tight_layout()\n",
            "plt.savefig(\"figures/rf_accuracy_vs_depth.png\", dpi=300)\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Step 7: Out-of-Bag (OOB) Error Decline Tracking\n",
            "Tracking the asymptotic reduction of OOB Error as tree bounds scale from 30 to 200.\n",
            "*(Uses warm_start=True to incrementally grow trees in seconds instead of retraining from scratch)*"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "tree_range = list(range(30, 201, 10))\n",
            "oob_errors = []\n",
            "\n",
            "print(\"[INFO] Tracking OOB Error across 30 to 200 trees (fast incremental growth)...\")\n",
            "rf_oob = RandomForestClassifier(\n",
            "    warm_start=True,\n",
            "    oob_score=True,\n",
            "    bootstrap=True,\n",
            "    random_state=42,\n",
            "    n_jobs=-1\n",
            ")\n",
            "\n",
            "for n in tree_range:\n",
            "    rf_oob.set_params(n_estimators=n)\n",
            "    rf_oob.fit(X_train, y_train)\n",
            "    oob_err = 1.0 - rf_oob.oob_score_\n",
            "    oob_errors.append(oob_err)\n",
            "\n",
            "min_oob_idx = int(np.argmin(oob_errors))\n",
            "best_tree_count = tree_range[min_oob_idx]\n",
            "min_oob_error = oob_errors[min_oob_idx]\n",
            "\n",
            "plt.figure(figsize=(7.5, 4.5))\n",
            "plt.plot(tree_range, oob_errors, marker='D', color='#d62728', lw=2, markersize=5)\n",
            "plt.scatter([best_tree_count], [min_oob_error], color='#8c564b', s=100, zorder=5, label=f'Min OOB: {min_oob_error:.4f} @ n={best_tree_count}')\n",
            "plt.title(\"Out-of-Bag (OOB) Error Decline Tracking Curve\", fontweight='bold')\n",
            "plt.xlabel(\"Ensemble Tree Bounds (n_estimators)\")\n",
            "plt.ylabel(\"Out-of-Bag (OOB) Error\")\n",
            "plt.grid(True, linestyle='--', alpha=0.6)\n",
            "plt.legend()\n",
            "plt.tight_layout()\n",
            "plt.savefig(\"figures/rf_oob_error_decline.png\", dpi=300)\n",
            "plt.show()\n",
            "\n",
            "print(f\"[SUCCESS] Lowest OOB Error: {min_oob_error:.4f} achieved at n_estimators={best_tree_count}\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Step 8: Comprehensive 5-Fold GridSearchCV Optimization\n",
            "Optimizing tree count, depth, leaf parameters, and subspace projection with live progress updates."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "param_grid = {\n",
            "    'n_estimators': [100, 150, 200],\n",
            "    'max_depth': [20, 30, None],\n",
            "    'min_samples_split': [2, 5],\n",
            "    'max_features': ['sqrt', 'log2']\n",
            "}\n",
            "\n",
            "print(\"[INFO] Starting 5-Fold GridSearchCV across hyperparameter grid...\")\n",
            "grid = GridSearchCV(\n",
            "    RandomForestClassifier(random_state=42, n_jobs=-1, oob_score=True, bootstrap=True),\n",
            "    param_grid=param_grid,\n",
            "    cv=5,\n",
            "    scoring='f1',\n",
            "    n_jobs=-1,\n",
            "    verbose=2\n",
            ")\n",
            "\n",
            "t0 = time.time()\n",
            "grid.fit(X_train, y_train)\n",
            "print(f\"\\n[SUCCESS] GridSearchCV completed in {time.time() - t0:.2f} seconds!\")\n",
            "print(f\"Best Parameters: {grid.best_params_}\")\n",
            "print(f\"Best 5-Fold CV F1-Score: {grid.best_score_:.4f}\")\n",
            "\n",
            "best_rf = grid.best_estimator_"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Step 9: Mean Decrease in Gini Impurity (MDI) Ranking for 30 Features\n",
            "Ranking diagnostic structural relevance across all 30 URL features."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "mdi_importances = best_rf.feature_importances_\n",
            "importance_df = pd.DataFrame({\n",
            "    \"Feature\": X.columns,\n",
            "    \"MDI_Importance\": mdi_importances\n",
            "}).sort_values(by=\"MDI_Importance\", ascending=False).reset_index(drop=True)\n",
            "\n",
            "importance_df[\"Rank\"] = importance_df.index + 1\n",
            "importance_df.to_csv(\"results/feature_importance_30.csv\", index=False)\n",
            "\n",
            "# Plot all 30 features\n",
            "plt.figure(figsize=(9, 10))\n",
            "colors = plt.cm.viridis(np.linspace(0.2, 0.85, len(importance_df)))\n",
            "plt.barh(importance_df[\"Feature\"][::-1], importance_df[\"MDI_Importance\"][::-1], color=colors)\n",
            "plt.xlabel(\"Mean Decrease in Gini Impurity (MDI)\", fontweight='bold')\n",
            "plt.title(\"Diagnostic Structural Weights of 30 URL Features\", fontweight='bold')\n",
            "plt.grid(axis='x', linestyle='--', alpha=0.6)\n",
            "plt.tight_layout()\n",
            "plt.savefig(\"figures/rf_feature_importance_30.png\", dpi=300)\n",
            "plt.show()\n",
            "\n",
            "print(\"Top 5 Discriminative Features:\")\n",
            "display(importance_df.head(5))"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Step 10: Performance Evaluation & Confusion Matrix\n",
            "Compute final test set accuracy, precision, recall, F1, specificity, and ROC-AUC."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Hardware Timing\n",
            "t_train_start = time.perf_counter()\n",
            "best_rf.fit(X_train, y_train)\n",
            "training_time = time.perf_counter() - t_train_start\n",
            "\n",
            "t_infer_start = time.perf_counter()\n",
            "y_pred = best_rf.predict(X_test)\n",
            "total_infer_time = time.perf_counter() - t_infer_start\n",
            "latency_us = (total_infer_time / len(X_test)) * 1_000_000\n",
            "\n",
            "y_prob = best_rf.predict_proba(X_test)[:, 1]\n",
            "cm = confusion_matrix(y_test, y_pred)\n",
            "\n",
            "acc = accuracy_score(y_test, y_pred)\n",
            "prec = precision_score(y_test, y_pred)\n",
            "rec = recall_score(y_test, y_pred)\n",
            "f1 = f1_score(y_test, y_pred)\n",
            "roc_auc = roc_auc_score(y_test, y_prob)\n",
            "\n",
            "print(\"=== FINAL HYPER-TUNED RANDOM FOREST RESULTS ===\")\n",
            "print(f\"Accuracy : {acc*100:.2f}%\")\n",
            "print(f\"Precision: {prec*100:.2f}%\")\n",
            "print(f\"Recall   : {rec*100:.2f}%\")\n",
            "print(f\"F1-Score : {f1*100:.2f}%\")\n",
            "print(f\"ROC-AUC  : {roc_auc:.4f}\")\n",
            "print(f\"Training Speed: {training_time:.4f} seconds\")\n",
            "print(f\"Per-Sample Latency: {latency_us:.2f} microseconds/sample\")\n",
            "\n",
            "# Confusion Matrix Display\n",
            "fig, ax = plt.subplots(figsize=(5, 4))\n",
            "ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[\"Phishing (0)\", \"Legitimate (1)\"]).plot(ax=ax, cmap=\"Blues\")\n",
            "plt.title(\"Random Forest Confusion Matrix\", fontweight='bold')\n",
            "plt.tight_layout()\n",
            "plt.savefig(\"figures/rf_confusion_matrix.png\", dpi=300)\n",
            "plt.show()"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "### Step 11: Export Inter-Group Handovers\n",
            "Automatically generates formatted text and CSV summaries to share with Groups 1, 2, 3, and 4."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [
            "# Deliverable to Group 1 (Latency)\n",
            "with open(\"results/handovers/to_group1_summary.txt\", \"w\") as f:\n",
            "    f.write(f\"Training Time: {training_time:.4f} s\\n\")\n",
            "    f.write(f\"Total Inference Time: {total_infer_time:.6f} s\\n\")\n",
            "    f.write(f\"Latency per sample: {latency_us:.2f} microseconds/sample\\n\")\n",
            "\n",
            "# Deliverable to Group 3 (Leaderboard)\n",
            "leaderboard_df = pd.DataFrame([{\n",
            "    \"Model\": \"Random Forest (Group 5)\",\n",
            "    \"Accuracy (%)\": f\"{acc*100:.2f}%\",\n",
            "    \"Precision (%)\": f\"{prec*100:.2f}%\",\n",
            "    \"Recall (%)\": f\"{rec*100:.2f}%\",\n",
            "    \"F1-Score (%)\": f\"{f1*100:.2f}%\",\n",
            "    \"ROC-AUC\": f\"{roc_auc:.4f}\"\n",
            "}])\n",
            "leaderboard_df.to_csv(\"results/handovers/to_group3_leaderboard_metrics.csv\", index=False)\n",
            "\n",
            "print(\"[SUCCESS] Handover files ready in results/handovers/!\")"
        ]
    }
]

notebook_dict = {
    "cells": cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.10.11"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(notebook_dict, f, indent=2)

print("Created notebook successfully at:", notebook_path)
