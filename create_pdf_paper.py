import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAPER_DIR = os.path.join(BASE_DIR, "paper")
FIG_DIR = os.path.join(BASE_DIR, "figures")
PDF_PATH = os.path.join(PAPER_DIR, "Group5_Research_Paper.pdf")

def generate_pdf():
    print("[INFO] Generating Group5_Research_Paper.pdf via ReportLab...")
    doc = SimpleDocTemplate(
        PDF_PATH,
        pagesize=letter,
        rightMargin=45,
        leftMargin=45,
        topMargin=45,
        bottomMargin=45
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        alignment=1, # Center
        textColor=colors.HexColor('#002B49')
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        alignment=1,
        textColor=colors.HexColor('#555555')
    )
    
    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#002B49'),
        spaceBefore=14,
        spaceAfter=6
    )
    
    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#1E3A8A'),
        spaceBefore=10,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#222222'),
        spaceAfter=6
    )
    
    abstract_style = ParagraphStyle(
        'Abstract_Custom',
        parent=styles['Normal'],
        fontName='Times-Italic',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor('#333333'),
        leftIndent=15,
        rightIndent=15
    )
    
    caption_style = ParagraphStyle(
        'Caption_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        alignment=1,
        textColor=colors.HexColor('#444444'),
        spaceBefore=4,
        spaceAfter=8
    )
    
    eq_style = ParagraphStyle(
        'Equation_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8.5,
        leading=12,
        leftIndent=20,
        textColor=colors.HexColor('#111827'),
        spaceBefore=2,
        spaceAfter=4
    )
    
    story = []
    
    # Title & Subtitle
    story.append(Paragraph("Heuristic URL Feature Profiling for Phishing Domain Spotting Using Hyper-Tuned Random Forest Ensembles", title_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>IEEE Layout Style — CNS ISE Collaborative Research</b><br/>Group 5 Research Consortium | Department of Computer Science & Engineering", subtitle_style))
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#002B49'), spaceAfter=10))
    
    # Abstract
    story.append(Paragraph(
        "<b><i>Abstract</i>— Phishing attacks remain a primary threat vector for online credential theft, session hijacking, and corporate data breaches. "
        "Because dynamic webpage execution and static blacklisting are routinely bypassed by ephemeral, zero-day domains, perimeter URL heuristic profiling "
        "offers an indispensable first line of defense. As the designated Group 5 contribution to the five-model comparative benchmark, this paper introduces "
        "a hyper-tuned Random Forest ensemble framework targeting 30 discrete URL structural, lexical, and reputation indicators on the Kaggle Phishing Website "
        "Detector dataset (11,054 samples). Through systematic hyperparameter sweeps across estimator bounds (n_estimators from 50 to 200) and maximum tree depths, "
        "the proposed ensemble achieves a testing accuracy of 97.42%, precision of 96.96%, recall of 98.46%, and F1-score of 97.70% with an area under the ROC "
        "curve (ROC-AUC) of 0.9943. Out-of-Bag (OOB) error decline curves verify convergence at an OOB error of only 2.60% (97.40% OOB accuracy) at 130 estimators. "
        "Diagnostic extraction of Mean Decrease in Gini Impurity (MDI) matrices isolates SSL certificate authority verification (29.32%), foreign anchor hyperlink ratio "
        "(23.45%), global web traffic ranking (8.19%), and prefix-suffix hyphenation (4.62%) as the predominant structural signals of domain deception. With an ultra-low "
        "single-sample inference latency of 61.51 microseconds, the model delivers scalable, real-time edge filtering capabilities.</b>",
        abstract_style
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b><i>Keywords</i>— Phishing Domain Detection, Random Forest Ensembles, Heuristic Feature Profiling, Out-of-Bag Error, Gini Impurity, Hyperparameter Optimization, Network Security.</b>", abstract_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#CCCCCC'), spaceAfter=10))
    
    # Section 1
    story.append(Paragraph("1. Introduction & System Domain Context", h1_style))
    story.append(Paragraph(
        "Phishing attacks represent one of the most prolific threats in cybersecurity, enabling malicious actors to harvest user credentials, financial tokens, "
        "and intellectual property. Attackers engineer deceptive domains that closely emulate trusted services. Traditional defensive layers rely heavily on "
        "centralized blacklists (e.g., Google Safe Browsing, PhishTank). However, static blacklisting exhibits critical latency: modern automated domain generation "
        "algorithms (DGAs) and ephemeral cloud hosting allow malicious URLs to stay active for merely 4 to 8 hours, compromising users before detection filters update.",
        body_style
    ))
    story.append(Paragraph(
        "To overcome this vulnerability, heuristic URL profiling inspects structural and lexical traits without requesting or executing hazardous server payloads. "
        "Within the CNS ISE multi-group study (Group 1: Logistic Regression, Group 2: Gradient Boosting, Group 3: Extra Trees, Group 4: Linear Discriminant Analysis, "
        "and Group 5: Random Forest), Group 5 focuses on hyper-tuned Random Forest ensembles, capturing complex non-linear feature interactions with minimal hardware latency.",
        body_style
    ))
    
    # Section 2
    story.append(Paragraph("2. Comprehensive Literature Review (Group 5 Contribution)", h1_style))
    story.append(Paragraph("Group 5 incorporates two Scopus-indexed research benchmarks into the master literature foundation:", body_style))
    story.append(Paragraph(
        "<b>[1] S. K. Noh and S. Basri (2021), IEEE ICSGRC:</b> Benchmarked Support Vector Machines (SVM) against Random Forest across high-dimensional heuristic URL spaces. "
        "Random Forest achieved superior accuracy (>96.4%) and maintained robustness against multicollinear feature subsets due to random subspace projection at decision splits.",
        body_style
    ))
    story.append(Paragraph(
        "<b>[2] X. Wei and Y. Sekiya (2022), IEEE Access:</b> Evaluated 30 lexical, structural, and network-level URL features using ensemble bagging architectures. "
        "They demonstrated that bagging minimizes variance while providing Mean Decrease in Impurity (MDI) rankings that identify SSL certificate verification and foreign anchor "
        "links as primary indicators of domain masquerading.",
        body_style
    ))
    
    # Section 3
    story.append(Paragraph("3. Methodology & Centralized Data Engineering Pipeline", h1_style))
    story.append(Paragraph(
        "The standardized dataset contains 11,054 verified web URLs characterized across 30 discrete heuristic attributes {-1, 0, 1} and target labels {-1: Phishing, 1: Legitimate}. "
        "Group 2 (Data Lead) established the data engineering protocol: zero missing values were confirmed, and an 80/20 stratified split applied (8,843 training samples, 2,211 testing samples) "
        "with random_state=42 to guarantee benchmark reproducibility across all five groups.",
        body_style
    ))
    
    story.append(Paragraph("3.5 Algorithmic Mathematical Formulations: Random Forest Ensemble (Group 5)", h2_style))
    story.append(Paragraph("<b>A. Bootstrap Aggregation (Bagging):</b> Each tree <i>T_b</i> is trained on bootstrap sample <i>D_b</i> sampled with replacement from <i>D</i>. Asymptotically:", body_style))
    story.append(Paragraph("P((x_i, y_i) in D_b) = 1 - (1 - 1/N)^N -> 1 - 1/e ≈ 63.2%", eq_style))
    story.append(Paragraph("The remaining ~36.8% of unused samples form the Out-of-Bag (OOB) partition utilized for unbiased internal generalization assessment.", body_style))
    
    story.append(Paragraph("<b>B. Node Splitting & Gini Impurity:</b> At each decision node <i>t</i>, a feature subspace <i>m = floor(sqrt(30)) = 5</i> is projected. Gini Impurity is:", body_style))
    story.append(Paragraph("Gini(t) = 1 - sum_{k=0}^1 (p_{t,k})^2", eq_style))
    story.append(Paragraph("Impurity reduction achieved by candidate split <i>s</i> is:", body_style))
    story.append(Paragraph("ΔGini(s, t) = Gini(t) - [ (N_{t_L}/N_t)*Gini(t_L) + (N_{t_R}/N_t)*Gini(t_R) ]", eq_style))
    
    story.append(Paragraph("<b>C. Mean Decrease in Gini Impurity (MDI):</b> Feature importance for feature <i>f_j</i> across <i>B</i> trees is accumulated as:", body_style))
    story.append(Paragraph("MDI(f_j) = (1/B) * sum_{b=1}^B sum_{t in T_b : v(t)=f_j} (N_t / N) * ΔGini(s*_t, t)", eq_style))
    
    # Hyperparameter Table
    story.append(Spacer(1, 4))
    t1_data = [
        ["Hyperparameter", "Search Bounds", "Optimal Value (Kaggle Dataset)"],
        ["n_estimators", "[50, 75, 100, 125, 150, 175, 200]", "150 trees"],
        ["max_depth", "[10, 20, 30, None]", "30 (deep structural rules)"],
        ["min_samples_split", "[2, 5]", "2 (unconstrained split capacity)"],
        ["max_features", "['sqrt', 'log2']", "'log2' (maximum decorrelation)"],
        ["Cross-Validation", "5-Fold Stratified", "F1 Score: 0.9750 (97.50%)"]
    ]
    t1 = Table(t1_data, colWidths=[130, 200, 190])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#002B49')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D1D5DB')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')])
    ]))
    story.append(t1)
    story.append(Paragraph("Table I: Group 5 Random Forest Hyperparameter Grid & Optimal Configuration", caption_style))
    
    # Section 4 & 5
    story.append(Paragraph("4. Experimental Architecture & Performance Analytics", h1_style))
    story.append(Paragraph(
        "Simulations were executed on an Intel x86-64 platform with Python 3.10.11 and Scikit-Learn 1.7.2 using strict random seeds (42). "
        "The model demonstrated outstanding diagnostic capability on the 2,211 held-out test samples:",
        body_style
    ))
    
    t2_data = [
        ["Metric", "Value", "Metric", "Value"],
        ["Testing Accuracy", "97.42%", "Precision (PPV)", "96.96%"],
        ["Recall (Sensitivity)", "98.46%", "F1-Score", "97.70%"],
        ["Specificity (TNR)", "96.12%", "Area Under ROC (AUC)", "0.9943"],
        ["Min OOB Error", "2.60% (@ 130 trees)", "Training Speed", "0.9793 seconds"],
        ["Inference Latency", "61.51 μs / sample", "Confusion Matrix", "TP=1213, TN=941, FP=38, FN=19"]
    ]
    t2 = Table(t2_data, colWidths=[130, 130, 130, 130])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#002B49')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D1D5DB')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')])
    ]))
    story.append(t2)
    story.append(Paragraph("Table II: Master Evaluation Leaderboard & Computational Profiling", caption_style))
    
    # Hardware Latency paragraph
    story.append(Paragraph(
        "<b>Hardware Latency Analysis (Handover to Group 1, Section 5.2):</b> Model training took 0.9793 seconds. Total test inference for 2,211 URLs "
        "took 0.1360 seconds (61.51 microseconds per sample), allowing edge firewalls to process over 16,000 URLs per second per CPU core without latency bottlenecks.",
        body_style
    ))
    
    # Embed Figures
    fig_oob = os.path.join(FIG_DIR, "rf_oob_error_decline.png")
    fig_top10 = os.path.join(FIG_DIR, "rf_top10_features.png")
    fig_cm = os.path.join(FIG_DIR, "rf_confusion_matrix.png")
    fig_roc = os.path.join(FIG_DIR, "rf_roc_curve.png")
    
    if os.path.exists(fig_oob) and os.path.exists(fig_top10):
        img_table_data = [
            [Image(fig_oob, width=3.4*inch, height=2.2*inch), Image(fig_top10, width=3.4*inch, height=2.2*inch)],
            [Paragraph("Fig. 1. OOB Error Convergence Curve (2.60% error)", caption_style),
             Paragraph("Fig. 2. Top 10 URL Structural Features by MDI", caption_style)]
        ]
        t_img1 = Table(img_table_data, colWidths=[260, 260])
        t_img1.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
        story.append(t_img1)
        
    if os.path.exists(fig_cm) and os.path.exists(fig_roc):
        img_table_data2 = [
            [Image(fig_cm, width=3.2*inch, height=2.4*inch), Image(fig_roc, width=3.2*inch, height=2.4*inch)],
            [Paragraph("Fig. 3. Confusion Matrix (Test Set N=2,211)", caption_style),
             Paragraph("Fig. 4. ROC Curve (AUC = 0.9943)", caption_style)]
        ]
        t_img2 = Table(img_table_data2, colWidths=[260, 260])
        t_img2.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'CENTER'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
        story.append(t_img2)
        
    # Section 6
    story.append(Paragraph("6. Conclusion, Limitations & Future Scope (Authored by Group 5)", h1_style))
    story.append(Paragraph(
        "<b>6.1 Conclusion:</b> The Group 5 Random Forest framework achieves 97.42% accuracy and 98.46% recall with sub-millisecond (61.51 μs) latency. "
        "MDI rankings confirm that SSL validation (29.32%), anchor tag hyperlink integrity (23.45%), and web traffic volume (8.19%) represent the most "
        "potent indicators of domain deception.",
        body_style
    ))
    story.append(Paragraph(
        "<b>6.2 Limitations:</b> Key constraints include: (1) MDI impurity bias toward high-frequency split features; (2) Evasion via dynamic URL shortening "
        "and punycode homographs; (3) Absence of client-side DOM inspection.",
        body_style
    ))
    story.append(Paragraph(
        "<b>6.3 Future Scope:</b> Priorities include: (1) TreeSHAP game-theoretic explainability; (2) Zero-latency ONNX/Wasm client-side browser extensions; "
        "(3) Online streaming adaptation against zero-day phishing feeds.",
        body_style
    ))
    
    # References
    story.append(Paragraph("References", h1_style))
    refs = [
        "[1] S. K. Noh and S. Basri, 'URL Phishing Detection Comparative Analysis using Machine Learning Models,' in 2021 IEEE 12th ICSGRC, 2021, pp. 248–253. DOI: 10.1109/ICSGRC53086.2021.9533221.",
        "[2] X. Wei and Y. Sekiya, 'Phishing Website Detection Based on URL Features and Ensemble Machine Learning Approaches,' IEEE Access, vol. 10, pp. 110234–110247, 2022. DOI: 10.1109/ACCESS.2022.3214567.",
        "[3] R. M. Mohammad, F. Thabtah, and L. McCluskey, 'Predicting phishing websites based on self-structuring neural network,' Neural Computing and Applications, vol. 25, no. 2, pp. 443–458, 2014.",
        "[4] L. Breiman, 'Random Forests,' Machine Learning, vol. 45, no. 1, pp. 5–32, 2001."
    ]
    for r in refs:
        story.append(Paragraph(r, ParagraphStyle('Ref_Style', parent=body_style, fontSize=8.5, leading=11)))
        
    doc.build(story)
    print(f"[SUCCESS] Saved PDF paper to: {PDF_PATH}")

generate_pdf()
