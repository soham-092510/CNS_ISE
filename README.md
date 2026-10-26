# CNS ISE - Group 5 Complete Project Guide
**Target Search Framework:** *"Heuristic URL Feature Profiling for Phishing Domain Spotting Using Hyper-Tuned Random Forest Ensembles"* (IEEE Layout Style)

---

## ⚡ 1-COPY COMMAND (Run All at Once)

Copy and paste this single block into your **PowerShell** or **Command Prompt (CMD)** inside the project directory:

### For PowerShell (Recommended for Windows):
```powershell
pip install -r requirements.txt; python run_experiments.py; jupyter lab Group5_RandomForest_Phishing.ipynb
```

### For Command Prompt (CMD):
```cmd
pip install -r requirements.txt && python run_experiments.py && jupyter lab Group5_RandomForest_Phishing.ipynb
```

### Multi-line (Just copy and paste all 3 lines together):
```bash
pip install -r requirements.txt
python run_experiments.py
jupyter lab Group5_RandomForest_Phishing.ipynb
```

> **What this does in one shot:**
> 1. Installs all required packages (`scikit-learn`, `pandas`, `numpy`, `matplotlib`, `jupyterlab`).
> 2. Runs the complete Group 5 Random Forest experimental pipeline on `data/phishing.csv` (generates all 7 figures in `figures/`, all CSV tables in `results/`, and all handover packets in `results/handovers/`).
> 3. Launches Jupyter Lab with `Group5_RandomForest_Phishing.ipynb` automatically opened in your browser!

---

## 🚀 Quick Start (In 3 Simple Steps)

### Step 1: Download the Kaggle Dataset
1. Visit the Kaggle dataset link: [Phishing Website Detector](https://www.kaggle.com/datasets/eswarchandt/phishing-website-detector)
2. Download the CSV file (typically named `phishing.csv` or `dataset.csv`).
3. Place that CSV file inside the **`data/`** folder:
   ```
   CNS ISE/
   └── data/
       └── phishing.csv  <-- Place your downloaded file here!
   ```
*(Note: A realistic 30-feature starter dataset is already generated in `data/phishing_sample.csv`, so the code works out of the box even before downloading!)*

---

### Step 2: Run the Notebook in Jupyter Lab (or 1-Click Script)

#### Option A: Run in Jupyter Lab
1. Open terminal / command prompt in this directory.
2. Run:
   ```bash
   jupyter lab Group5_RandomForest_Phishing.ipynb
   ```
3. In Jupyter Lab, click **Run > Run All Cells**.

#### Option B: 1-Click Execution from Terminal
If you just want to generate all figures, tables, and handovers in one second:
```bash
python run_experiments.py
```

Everything will automatically run:
- Baseline Random Forest classifier
- Hyperparameter sweep (50 to 200 trees, maximum depth ranges)
- Out-of-Bag (OOB) error decline tracking plot
- Mean Decrease in Gini Impurity (MDI) ranking for all 30 features
- 5-Fold `GridSearchCV` hyperparameter tuning
- Training time & single-sample inference latency benchmark
- Confusion matrix & ROC curve

---

### Step 3: Send Deliverables to Other Groups

All handovers are already pre-formatted and saved in **`results/handovers/`**:

| Group | Handover Files | Purpose in Report |
|---|---|---|
| **Group 1** | `results/handovers/to_group1_summary.txt`<br>`results/handovers/to_group1_latency_overhead.csv` | **Section 5.2**: Computational Overhead & Hardware Latency Analysis (Training time: ~0.68s, Sample Latency: ~320 $\mu$s). |
| **Group 2** | `results/handovers/to_group2_data_spec.txt` | **Section 3.1**: Data Engineering & Preprocessing Confirmation (30 features, stratified 80/20 split, zero nulls). |
| **Group 3** | `results/handovers/to_group3_summary.txt`<br>`results/handovers/to_group3_leaderboard_metrics.csv` | **Section 5.1**: Performance Analytics Tournament Leaderboard (Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrix). |
| **Group 4** | `results/handovers/to_group4_system_architecture.txt` | **Section 4**: Experimental Simulation Architecture Setup (Python 3.10, Scikit-learn 1.7.2, Windows/CPU specs). |

---

## 📄 Your Academic Paper Sections (IEEE Format)

All LaTeX files are written and located in the **`paper/`** folder:

1. **`paper/section1_intro.tex`**:
   - **Section 1: Introduction & System Domain Context** (Drafted by Group 5).
   - Covers problem scope, why static blacklists fail on zero-day domains, why URL heuristic profiling works, and the system domain architecture.

2. **`paper/section2_literature.tex` & `paper/references.bib`**:
   - **Section 2: Comprehensive Literature Review** (Group 5 Contribution).
   - Contains 2 genuine Scopus-indexed papers:
     1. *Noh & Basri (2021 IEEE)*: URL phishing comparative analysis using Random Forest.
     2. *Wei & Sekiya (2022 IEEE Access)*: Ensemble machine learning with 30 URL features.
   - BibTeX citation entries in `paper/references.bib` ready to copy into your team's master `.bib` file.

3. **`paper/section3_5_random_forest.tex`**:
   - **Section 3.5: Algorithmic Mathematical Formulations (Random Forest)**.
   - Equations for:
     - Bootstrap Aggregation ($P = 1 - e^{-1} \approx 63.2\%$).
     - Gini Impurity: $I_G(t) = 1 - \sum p_{t,k}^2$.
     - Impurity Reduction: $\Delta I_G(s, t)$.
     - Subspace feature projection: $m = \sqrt{M} \approx 5$.
     - Ensemble Majority Voting: $\hat{y} = \text{mode}\{T_1(x), \dots, T_B(x)\}$.
     - Out-of-Bag (OOB) error estimation formula.
     - Mean Decrease in Gini Impurity (MDI) weight formula.
     - Hyperparameter grid documentation table.

4. **`paper/section6_conclusion.tex`**:
   - **Section 6: Conclusion, Limitations & Future Research Scope** (Written exclusively by Group 5).
   - Synthesizes the 5-model tournament findings.
   - Details real-world limitations (MDI cardinality bias, zero-day adversarial obfuscation, absence of dynamic DOM payload).
   - Highlights future work (TreeSHAP explainability, Wasm/ONNX browser extensions, continual online learning).

5. **`paper/ieee_group5_manuscript.tex`**:
   - Complete, standalone compilable IEEE format paper for Group 5.

---

## 📊 Generated Publication Figures (`figures/`)

| Figure File | What It Shows |
|---|---|
| `figures/rf_oob_error_decline.png` | **OOB Error Decline Tracking**: Shows error declining and stabilizing as trees scale from 30 to 200. |
| `figures/rf_feature_importance_30.png` | **Mean Decrease in Gini Impurity (MDI)**: Complete ranking of all 30 URL features. |
| `figures/rf_top10_features.png` | **Top-10 Diagnostic Features**: Clean bar chart of highest-weighted phishing indicators (SSL, Anchor URL, Subdomain, etc.). |
| `figures/rf_confusion_matrix.png` | **Confusion Matrix**: Visualizing True Positives, True Negatives, False Positives, and False Negatives. |
| `figures/rf_accuracy_vs_trees.png` | **Parameter Sweep (Trees)**: Accuracy across $n_{\text{estimators}} \in [50, 200]$. |
| `figures/rf_accuracy_vs_depth.png` | **Parameter Sweep (Depth)**: Accuracy across maximum tree depths. |
| `figures/rf_roc_curve.png` | **ROC Curve**: Receiver Operating Characteristic curve with AUC score. |

---

## 📁 Project Directory Layout
```
CNS ISE/
├── data/
│   └── phishing_sample.csv             <-- Put your Kaggle phishing.csv here
├── figures/
│   ├── rf_accuracy_vs_depth.png
│   ├── rf_accuracy_vs_trees.png
│   ├── rf_confusion_matrix.png
│   ├── rf_feature_importance_30.png    <-- 30 URL Feature MDI Bar Chart
│   ├── rf_oob_error_decline.png        <-- Out-of-Bag Error Curve
│   ├── rf_roc_curve.png
│   └── rf_top10_features.png
├── paper/
│   ├── ieee_group5_manuscript.tex      <-- Master IEEE Paper
│   ├── references.bib                  <-- 2 Scopus Papers (BibTeX)
│   ├── section1_intro.tex              <-- Section 1 draft
│   ├── section2_literature.tex         <-- Section 2 review
│   ├── section3_5_random_forest.tex    <-- Section 3.5 equations & grid
│   └── section6_conclusion.tex         <-- Section 6 conclusion
├── results/
│   ├── feature_importance_30.csv       <-- Exact MDI weights for all 30 features
│   ├── hyperparameter_grid_results.csv <-- 5-Fold GridSearchCV log
│   ├── rf_final_performance_metrics.csv<-- Final accuracy, precision, F1, latency
│   ├── rf_oob_error_tracking.csv       <-- OOB error values
│   ├── sweep_max_depth.csv
│   ├── sweep_n_estimators.csv
│   └── handovers/                      <-- READY TO SEND TO GROUPS 1, 2, 3, 4!
│       ├── to_group1_latency_overhead.csv
│       ├── to_group1_summary.txt
│       ├── to_group2_data_spec.txt
│       ├── to_group3_leaderboard_metrics.csv
│       ├── to_group3_summary.txt
│       └── to_group4_system_architecture.txt
├── Group5_RandomForest_Phishing.ipynb  <-- Main Jupyter Lab Notebook
├── run_experiments.py                  <-- 1-Click Execution Script
├── requirements.txt                    <-- Dependencies
└── README.md                           <-- This Guide
```
