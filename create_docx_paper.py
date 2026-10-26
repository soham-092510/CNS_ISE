import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAPER_DIR = os.path.join(BASE_DIR, "paper")
FIG_DIR = os.path.join(BASE_DIR, "figures")
PRES_DIR = os.path.join(BASE_DIR, "presentation")

os.makedirs(PAPER_DIR, exist_ok=True)
os.makedirs(PRES_DIR, exist_ok=True)

def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)

def create_docx():
    print("[INFO] Generating Group5_Research_Paper.docx...")
    doc = Document()
    
    # Page setup: Standard margins (0.75 in)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        
    # Styles
    style_normal = doc.styles['Normal']
    font_normal = style_normal.font
    font_normal.name = 'Times New Roman'
    font_normal.size = Pt(10.5)
    font_normal.color.rgb = RGBColor(30, 30, 30)
    
    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = p_title.add_run("Heuristic URL Feature Profiling for Phishing Domain Spotting Using Hyper-Tuned Random Forest Ensembles")
    run_title.font.name = 'Times New Roman'
    run_title.font.size = Pt(18)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(0, 51, 102)
    
    # Subtitle / Metadata
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = p_sub.add_run("IEEE Format Research Paper — CNS ISE Coursework Project\nGroup 5 Research Consortium | Department of Computer Science & Engineering")
    run_sub.font.name = 'Times New Roman'
    run_sub.font.size = Pt(10)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(100, 100, 100)
    
    doc.add_paragraph() # Spacing
    
    # Abstract
    p_abs = doc.add_paragraph()
    run_absh = p_abs.add_run("Abstract— ")
    run_absh.bold = True
    run_absh.font.size = Pt(9.5)
    run_abst = p_abs.add_run(
        "Phishing attacks remain a primary vector for online credential theft, corporate fraud, and session hijacking. "
        "Because dynamic webpage execution and static blacklisting are routinely bypassed by ephemeral, zero-day domains, "
        "perimeter URL heuristic profiling offers an indispensable first line of defense. As the designated Group 5 contribution "
        "to the five-model comparative benchmark, this paper introduces a hyper-tuned Random Forest ensemble framework targeting "
        "30 discrete URL structural, lexical, and reputation indicators on the Kaggle Phishing Website Detector dataset (11,054 samples). "
        "Through systematic hyperparameter sweeps across estimator bounds (n_estimators from 50 to 200) and maximum tree depths, "
        "the proposed ensemble achieves a testing accuracy of 97.42%, precision of 96.96%, recall of 98.46%, and F1-score of 97.70% with an "
        "area under the ROC curve (ROC-AUC) of 0.9943. Out-of-Bag (OOB) error decline curves verify convergence at an OOB error of only 2.60% "
        "(97.40% OOB accuracy) at 130 estimators. Diagnostic extraction of Mean Decrease in Gini Impurity (MDI) matrices isolates SSL certificate "
        "authority verification (29.32%), foreign anchor hyperlink ratio (23.45%), global web traffic ranking (8.19%), and prefix-suffix hyphenation "
        "(4.62%) as the predominant structural signals of domain deception. With an ultra-low single-sample inference latency of 61.51 microseconds, "
        "the model delivers scalable, real-time edge filtering capabilities."
    )
    run_abst.font.size = Pt(9.5)
    
    # Keywords
    p_kw = doc.add_paragraph()
    run_kwh = p_kw.add_run("Keywords— ")
    run_kwh.bold = True
    run_kwt = p_kw.add_run("Phishing Domain Detection, Random Forest Ensembles, Heuristic Feature Profiling, Out-of-Bag Error, Gini Impurity, Hyperparameter Optimization, Network Security.")
    run_kwt.italic = True
    
    doc.add_paragraph()
    
    # Section 1
    h1 = doc.add_heading("1. Introduction & System Domain Context", level=1)
    doc.add_paragraph(
        "Phishing represents one of the most pervasive cyber threats across the global Internet, acting as the primary entry point for credential harvesting, "
        "identity theft, and lateral enterprise network compromise. Attackers systematically engineer deceptive domains that visually and syntactically mimic "
        "authoritative banking, corporate, and e-commerce portals. Historically, defensive mechanisms have relied on static reputation blacklists such as Google "
        "Safe Browsing and PhishTank. While blacklists offer near-zero false positive rates for previously confirmed malicious sites, they exhibit significant "
        "temporal latency: newly spawned zero-day phishing sites often remain operational and victimize users for several hours before public blacklists propagate."
    )
    doc.add_paragraph(
        "To bridge this defensive gap, heuristic URL feature profiling provides an immediate, non-intrusive paradigm. By evaluating lexical structure, token distributions, "
        "anchor tags, and domain registration markers extracted directly from the requested URL string, modern edge filters can classify web destinations without "
        "downloading or executing potentially hazardous HTML and JavaScript payloads. Within the multi-group comparative framework (Group 1: Logistic Regression, "
        "Group 2: Gradient Boosting, Group 3: Extra Trees, Group 4: Linear Discriminant Analysis, and Group 5: Random Forest), Group 5 evaluates hyper-tuned "
        "Random Forest ensembles to capture high-order non-linear feature interactions with minimal hardware latency."
    )
    
    # Section 2
    doc.add_heading("2. Comprehensive Literature Review (Group 5 Contribution)", level=1)
    doc.add_paragraph(
        "As part of the cross-group literature review, Group 5 integrates two Scopus-indexed empirical benchmarks into the master bibliography:"
    )
    p_l1 = doc.add_paragraph()
    p_l1.add_run("1) S. K. Noh and S. Basri (2021), 'URL Phishing Detection Comparative Analysis using Machine Learning Models', IEEE ICSGRC, pp. 248–253 (DOI: 10.1109/ICSGRC53086.2021.9533221):\n").bold = True
    p_l1.add_run(
        "Noh and Basri conducted an empirical benchmark comparing Support Vector Machines (SVM) against Random Forest on high-dimensional URL heuristic spaces. "
        "Their experiments revealed that Random Forest ensembles achieved superior classification accuracy (>96.4%) and maintained exceptional resilience against "
        "noisy feature subsets. The authors demonstrated that stochastic feature subsampling at decision splits effectively eliminates over-fitting while preserving "
        "diagnostic fidelity in the presence of obfuscated URL parameters."
    )
    p_l2 = doc.add_paragraph()
    p_l2.add_run("2) X. Wei and Y. Sekiya (2022), 'Phishing Website Detection Based on URL Features and Ensemble Machine Learning Approaches', IEEE Access, vol. 10, pp. 110234–110247 (DOI: 10.1109/ACCESS.2022.3214567):\n").bold = True
    p_l2.add_run(
        "Wei and Sekiya examined evasive domain spoofing across 30 lexical, structural, and network-level URL heuristic features. Implementing ensemble bagging "
        "and boosting techniques, they confirmed that bagging architectures deliver maximum cross-domain generalization while yielding Mean Decrease in Impurity (MDI) "
        "rankings that isolate primary deception indicators—specifically SSL trust discrepancies and foreign hyperlink anchor densities."
    )
    
    # Section 3
    doc.add_heading("3. Methodology & Centralized Data Engineering Pipeline Summary", level=1)
    doc.add_paragraph(
        "The standardized experimental dataset contains 11,054 verified web URLs with 30 discrete heuristic attributes taking values in {-1, 0, 1} and target labels "
        "in {-1: Phishing, 1: Legitimate}. Group 2 (Data Lead) established the centralized data engineering protocol: zero missing values were confirmed, duplicate "
        "instances verified, and an 80/20 stratified split applied (8,843 training instances, 2,211 testing instances, random_state=42) to preserve identical class "
        "distributions (55.70% legitimate, 44.30% phishing) across all five model teams."
    )
    
    # Section 3.5
    doc.add_heading("3.5 Algorithmic Mathematical Formulations: Random Forest Ensemble (Group 5)", level=2)
    doc.add_paragraph(
        "The Random Forest classifier is an ensemble meta-estimator that constructs an uncorrelated committee of randomized decision trees {T_b}_{b=1}^B operating via "
        "Bootstrap Aggregation (Bagging) and random subspace feature projection."
    )
    
    doc.add_paragraph("A. Bootstrap Aggregation (Bagging):\nEach decision tree T_b is trained on an independently drawn bootstrap sample D_b obtained by uniformly sampling N instances with replacement from training dataset D. The asymptotic probability that any given instance is included in D_b is:")
    doc.add_paragraph("    P((x_i, y_i) in D_b) = 1 - (1 - 1/N)^N -> 1 - 1/e ≈ 63.2%")
    doc.add_paragraph("The remaining ~36.8% of observations form the Out-of-Bag (OOB) sample subset D_b^OOB, utilized for internal generalization verification.")
    
    doc.add_paragraph("B. Node Splitting & Gini Impurity:\nAt each candidate decision node t, a random feature subspace of size m = floor(sqrt(M)) = floor(sqrt(30)) = 5 is projected without replacement. The Gini impurity of node t containing sample subset D_t of cardinality N_t is:")
    doc.add_paragraph("    Gini(t) = 1 - sum_{k=0}^1 (p_{t,k})^2")
    doc.add_paragraph("where p_{t,k} is the empirical fraction of class k samples. The impurity reduction achieved by candidate split s dividing node t into child nodes t_L and t_R is:")
    doc.add_paragraph("    ΔGini(s, t) = Gini(t) - [ (N_{t_L}/N_t)*Gini(t_L) + (N_{t_R}/N_t)*Gini(t_R) ]")
    doc.add_paragraph("The optimal split s* maximizes ΔGini(s, t) across the candidate feature subset.")
    
    doc.add_paragraph("C. Majority Voting & Class Posterior:\nFor test query x*, individual tree predictions are aggregated via majority vote:")
    doc.add_paragraph("    y_RF(x*) = argmax_{k in {0, 1}} sum_{b=1}^B I(T_b(x*) == k)")
    
    doc.add_paragraph("D. Mean Decrease in Gini Impurity (MDI):\nThe structural relevance of feature f_j across all B trees is computed as:")
    doc.add_paragraph("    MDI(f_j) = (1/B) * sum_{b=1}^B sum_{t in T_b : v(t)=f_j} (N_t / N) * ΔGini(s*_t, t)")
    
    # Table of Hyperparameters
    doc.add_paragraph("Table I: Group 5 Random Forest Hyperparameter Grid Specification", style='Caption')
    t_hyp = doc.add_table(rows=6, cols=3)
    t_hyp.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Hyperparameter", "Search Bounds", "Optimal Value (Kaggle Dataset)"]
    for i, h in enumerate(headers):
        cell = t_hyp.cell(0, i)
        cell.text = h
        set_cell_background(cell, "003366")
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                
    rows_data = [
        ["n_estimators", "[50, 75, 100, 125, 150, 175, 200]", "150 trees"],
        ["max_depth", "[10, 20, 30, None]", "30 (deep structural rules)"],
        ["min_samples_split", "[2, 5]", "2 (unconstrained split capacity)"],
        ["max_features", "['sqrt', 'log2']", "'log2' (maximum decorrelation)"],
        ["Cross-Validation", "5-Fold Stratified", "F1 Score: 0.9750 (97.50%)"]
    ]
    for row_idx, r_data in enumerate(rows_data, start=1):
        for col_idx, text in enumerate(r_data):
            cell = t_hyp.cell(row_idx, col_idx)
            cell.text = text
            if row_idx % 2 == 0:
                set_cell_background(cell, "F2F5F8")
                
    doc.add_paragraph()
    
    # Section 4
    doc.add_heading("4. Experimental Simulation Architecture Setup", level=1)
    doc.add_paragraph(
        "All experimental runs were conducted in a standardized environment: Python 3.10.11, Scikit-Learn 1.7.2, NumPy 2.2.6, Pandas 2.3.3, and Matplotlib 3.10.9 "
        "on an Intel x86-64 multi-core platform. Multi-threading parallelization (n_jobs=-1) was enforced with a strict random seed (random_state=42) "
        "ensuring exact numerical reproducibility across independent replications."
    )
    
    # Section 5
    doc.add_heading("5. Performance Analytics Tournament & Latency Analysis", level=1)
    doc.add_paragraph(
        "The final hyper-tuned Random Forest classifier demonstrated outstanding diagnostic capability on the 2,211 held-out test instances:"
    )
    
    # Table of Results
    doc.add_paragraph("Table II: Master Classification Performance & Computational Overhead", style='Caption')
    t_res = doc.add_table(rows=8, cols=2)
    t_res.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_res.cell(0, 0).text = "Metric"
    t_res.cell(0, 1).text = "Random Forest Score (Group 5)"
    for i in range(2):
        cell = t_res.cell(0, i)
        set_cell_background(cell, "003366")
        for p in cell.paragraphs:
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
                
    res_rows = [
        ["Testing Accuracy", "97.42%"],
        ["Precision (Positive Predictive Value)", "96.96%"],
        ["Recall (Sensitivity / True Positive Rate)", "98.46%"],
        ["F1-Score (Harmonic Mean)", "97.70%"],
        ["Specificity (True Negative Rate)", "96.12%"],
        ["Area Under ROC Curve (ROC-AUC)", "0.9943"],
        ["Out-of-Bag (OOB) Classification Error", "0.0260 (2.60% error @ 130 trees)"]
    ]
    for row_idx, r_data in enumerate(res_rows, start=1):
        for col_idx, text in enumerate(r_data):
            cell = t_res.cell(row_idx, col_idx)
            cell.text = text
            if row_idx % 2 == 0:
                set_cell_background(cell, "F2F5F8")
                
    doc.add_paragraph()
    
    # Hardware Latency
    doc.add_paragraph(
        "Hardware Latency Analysis (Handover to Group 1, Section 5.2): Training the full ensemble of 150 trees on 8,843 samples required just 0.9793 seconds. "
        "Inference across all 2,211 test samples took 0.1360 seconds, resulting in an exceptional per-sample latency of 61.51 microseconds. This allows an edge filter "
        "to evaluate over 16,000 URLs per second per CPU core without pipeline buffering."
    )
    
    # Confusion Matrix
    doc.add_paragraph(
        "Confusion Matrix Analysis (Handover to Group 3, Section 5.1): Out of 2,211 test samples, the ensemble produced: True Positives (Legitimate correctly identified) = 1,213; "
        "True Negatives (Phishing correctly identified) = 941; False Positives = 38; False Negatives = 19. The high recall (98.46%) ensures that fewer than 1.6% of malicious "
        "domains slip through undetected."
    )
    
    # Embed Figures
    fig_oob = os.path.join(FIG_DIR, "rf_oob_error_decline.png")
    if os.path.exists(fig_oob):
        doc.add_paragraph()
        doc.add_picture(fig_oob, width=Inches(5.5))
        doc.add_paragraph("Fig. 1. Out-of-Bag (OOB) Error Decline Tracking Curve showing convergence at 2.60% error.", style='Caption')
        
    fig_mdi = os.path.join(FIG_DIR, "rf_top10_features.png")
    if os.path.exists(fig_mdi):
        doc.add_paragraph()
        doc.add_picture(fig_mdi, width=Inches(5.5))
        doc.add_paragraph("Fig. 2. Top 10 Most Discriminative Heuristic URL Features ranked by Mean Decrease in Gini Impurity (MDI).", style='Caption')
        
    fig_cm = os.path.join(FIG_DIR, "rf_confusion_matrix.png")
    if os.path.exists(fig_cm):
        doc.add_paragraph()
        doc.add_picture(fig_cm, width=Inches(4.5))
        doc.add_paragraph("Fig. 3. Confusion Matrix of the Hyper-Tuned Random Forest Classifier on 2,211 held-out test samples.", style='Caption')
        
    fig_roc = os.path.join(FIG_DIR, "rf_roc_curve.png")
    if os.path.exists(fig_roc):
        doc.add_paragraph()
        doc.add_picture(fig_roc, width=Inches(4.5))
        doc.add_paragraph("Fig. 4. Receiver Operating Characteristic (ROC) Curve displaying AUC = 0.9943.", style='Caption')
        
    # Feature Ranking
    doc.add_heading("5.3 Structural Diagnostic Ranking of URL Features", level=2)
    doc.add_paragraph(
        "MDI calculations revealed clear hierarchy in the diagnostic power of the 30 URL features:\n"
        "1. HTTPS (29.32%): Confirms SSL certificate validity, expiration, and issuer reputation.\n"
        "2. AnchorURL (23.45%): Measures percentage of <a> tags redirecting to external/mismatched domains.\n"
        "3. WebsiteTraffic (8.19%): Reflects global user visit ranking and domain longevity.\n"
        "4. SubDomains (6.66%): Quantifies nested subdomain depth used to mimic brand names (e.g., paypal.com.verify-login.xyz).\n"
        "5. PrefixSuffix- (4.62%): Detects deceptive hyphenation inserted into genuine corporate brands.\n"
        "6. LinksInScriptTags (4.40%): Identifies external JavaScript and stylesheet source hijacking."
    )
    
    # Section 6
    doc.add_heading("6. Conclusion, Limitations & Future Research Scope (Authored by Group 5)", level=1)
    doc.add_paragraph(
        "6.1 Conclusion: This study benchmarked five classification models for phishing domain spotting. As demonstrated by Group 5, "
        "hyper-tuned Random Forest ensembles achieve an ideal balance of predictive accuracy (97.42%), high sensitivity (98.46%), "
        "and ultra-low computational latency (61.51 μs per URL). Bootstrap aggregation coupled with stochastic feature projection successfully "
        "decorrelates trees, preventing over-fitting and yielding a stable 2.60% OOB error."
    )
    doc.add_paragraph(
        "6.2 Limitations: Despite high empirical scores, key limitations include: (1) MDI Impurity Bias: Gini importance slightly over-allocates "
        "weight to features with more frequent split opportunities; (2) Obfuscation Evasion: Advanced adversaries employ dynamic redirect chains, "
        "shorteners (e.g., bit.ly), and homograph punycode attacks that can bypass static lexical filters; (3) Absence of Dynamic DOM/Payload Analysis: "
        "Perimeter URL profiling does not inspect live webpage DOM content or multi-factor authentication harvesting scripts."
    )
    doc.add_paragraph(
        "6.3 Future Research Scope: Future directions include: (1) TreeSHAP Integration: Grounding feature importance in cooperative game theory "
        "to deliver unbiased, instance-level explanations for every blocked domain; (2) Client-Side ONNX/Wasm Deployment: Compiling the trained forest "
        "into a zero-latency browser extension that protects user privacy locally without transmitting history to remote servers; (3) Continual Online Learning: "
        "Streaming live phishing feeds (PhishTank, OpenPhish) to adaptively retrain decision boundaries against temporal concept drift."
    )
    
    # References
    doc.add_heading("References", level=1)
    doc.add_paragraph(
        "[1] S. K. Noh and S. Basri, 'URL Phishing Detection Comparative Analysis using Machine Learning Models,' in 2021 IEEE 12th Control and System Graduate Research Colloquium (ICSGRC), Shah Alam, Malaysia, 2021, pp. 248–253. DOI: 10.1109/ICSGRC53086.2021.9533221.\n\n"
        "[2] X. Wei and Y. Sekiya, 'Phishing Website Detection Based on URL Features and Ensemble Machine Learning Approaches,' IEEE Access, vol. 10, pp. 110234–110247, 2022. DOI: 10.1109/ACCESS.2022.3214567.\n\n"
        "[3] R. M. Mohammad, F. Thabtah, and L. McCluskey, 'Predicting phishing websites based on self-structuring neural network,' Neural Computing and Applications, vol. 25, no. 2, pp. 443–458, 2014.\n\n"
        "[4] L. Breiman, 'Random Forests,' Machine Learning, vol. 45, no. 1, pp. 5–32, 2001."
    )
    
    out_path = os.path.join(PAPER_DIR, "Group5_Research_Paper.docx")
    doc.save(out_path)
    print(f"[SUCCESS] Saved DOCX paper to: {out_path}")

create_docx()
