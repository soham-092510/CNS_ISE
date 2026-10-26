import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
PRES_DIR = os.path.join(BASE_DIR, "presentation")
PPTX_PATH = os.path.join(PRES_DIR, "Group5_Presentation.pptx")

os.makedirs(PRES_DIR, exist_ok=True)

prs = Presentation()
prs.slide_width = Inches(13.333) # 16:9 widescreen
prs.slide_height = Inches(7.5)

NAVY = RGBColor(0, 43, 73)
TEAL = RGBColor(0, 150, 180)
DARK_GRAY = RGBColor(40, 40, 40)
WHITE = RGBColor(255, 255, 255)
LIGHT_BG = RGBColor(245, 248, 250)
GREEN = RGBColor(34, 139, 34)

blank_layout = prs.slide_layouts[6]

def add_header(slide, title_text, category_text="CNS ISE — GROUP 5: RANDOM FOREST"):
    # Header bar
    top_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.1))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = NAVY
    top_bar.line.fill.background()
    
    tf = top_bar.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.8)
    tf.margin_top = Inches(0.12)
    
    p_cat = tf.paragraphs[0]
    p_cat.text = category_text.upper()
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = TEAL
    
    p_title = tf.add_paragraph()
    p_title.text = title_text
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = WHITE

# Slide 1: Title Slide
s1 = prs.slides.add_slide(blank_layout)
bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
bg1.fill.solid()
bg1.fill.fore_color.rgb = NAVY
bg1.line.fill.background()

tx1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.333), Inches(4.5))
tf1 = tx1.text_frame
tf1.word_wrap = True

p = tf1.paragraphs[0]
p.text = "CNS ISE PROJECT — GROUP 5"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = TEAL
p.space_after = Pt(14)

p2 = tf1.add_paragraph()
p2.text = "Heuristic URL Feature Profiling for Phishing Domain Spotting Using Hyper-Tuned Random Forest Ensembles"
p2.font.size = Pt(32)
p2.font.bold = True
p2.font.color.rgb = WHITE
p2.space_after = Pt(20)

p3 = tf1.add_paragraph()
p3.text = "• Model: Hyper-Tuned Random Forest (150 Trees, 30 Max Depth)\n• Dataset: Kaggle 11,054 Phishing & Legitimate URLs (30 Features)\n• Final Score: 97.42% Accuracy | 97.70% F1 | 61.5 μs Latency"
p3.font.size = Pt(18)
p3.font.color.rgb = RGBColor(220, 235, 245)

# Slide 2: The Problem in Simple Words
s2 = prs.slides.add_slide(blank_layout)
add_header(s2, "The Real-World Problem: Why Phishing Still Fools People")
tx2 = s2.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.5))
tf2 = tx2.text_frame
tf2.word_wrap = True

def add_bullet(tf, heading, body):
    p = tf.add_paragraph()
    p.text = "• " + heading + ": "
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = NAVY
    p.space_after = Pt(10)
    run = p.add_run()
    run.text = body
    run.font.bold = False
    run.font.color.rgb = DARK_GRAY

add_bullet(tf2, "What is Phishing?", "Fake websites built by attackers that look 100% like real banks, Google, or PayPal to steal passwords.")
add_bullet(tf2, "Why Traditional Blacklists Fail", "Companies like Google keep lists of bad websites, but attackers create new fake websites in minutes and kill them in 4 hours. By the time a site is added to a blacklist, thousands are already hacked.")
add_bullet(tf2, "Our Goal (The Big Picture)", "Can we detect fake websites instantly just by looking at the URL itself — before a user even opens the page?")
add_bullet(tf2, "Our Superpower (Group 5)", "We used Random Forest — an ensemble of 150 AI decision trees — to catch sneaky URL clues with 97.42% accuracy!")

# Slide 3: What Clues Did We Look At? (30 Features)
s3 = prs.slides.add_slide(blank_layout)
add_header(s3, "The 30 URL Clues We Analyzed (Without Opening the Page)")
tx3 = s3.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.5))
tf3 = tx3.text_frame
tf3.word_wrap = True
add_bullet(tf3, "Lexical & Address Clues", "Does it use an IP address instead of a domain? Is the URL ridiculously long? Does it use @ symbol or // redirects?")
add_bullet(tf3, "Suspicious Subdomains", "Does it have 4 subdomains like 'paypal.com.verify-account.login-secure.xyz' to trick mobile users?")
add_bullet(tf3, "SSL Certificate Checks", "Is HTTPS legitimate, or is it a self-signed fake certificate with mismatched authority?")
add_bullet(tf3, "Anchor & Link Behavior", "Do the buttons and links on the page actually point back to the real site, or to an attacker's server?")
add_bullet(tf3, "Domain Reputation", "Is the domain brand new (created 3 days ago)? Does it have zero web traffic on Alexa?")

# Slide 4: What is Random Forest? (Simple Analogy)
s4 = prs.slides.add_slide(blank_layout)
add_header(s4, "How Random Forest Works (The 150 Detective Analogy)")
tx4 = s4.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.5))
tf4 = tx4.text_frame
tf4.word_wrap = True
add_bullet(tf4, "A Single Decision Tree is Like 1 Detective", "One detective might make a mistake, have personal bias, or get tricked by an unusual clue.")
add_bullet(tf4, "Random Forest is a Committee of 150 Detectives", "We build 150 distinct trees. Each tree is trained on a different random subset of data (Bootstrap Sampling) and looks at different random clues (Subspace Projection).")
add_bullet(tf4, "Democratic Majority Voting", "When a URL arrives, all 150 trees vote: 'Phishing' or 'Safe'. If 140 say Phishing, the final verdict is Phishing! This completely removes individual mistakes.")
add_bullet(tf4, "The Secret Weapon (OOB Score)", "Because each tree only saw ~63% of samples, the remaining 37% (Out-of-Bag) act as an instant self-test without needing a separate test set.")

# Slide 5: Experimental Architecture & Figures (OOB & Top 10)
s5 = prs.slides.add_slide(blank_layout)
add_header(s5, "Out-of-Bag (OOB) Decline & Top Predictive Features")
fig1 = os.path.join(FIG_DIR, "rf_oob_error_decline.png")
fig2 = os.path.join(FIG_DIR, "rf_top10_features.png")

if os.path.exists(fig1):
    s5.shapes.add_picture(fig1, Inches(0.8), Inches(1.5), Inches(5.6), Inches(4.2))
if os.path.exists(fig2):
    s5.shapes.add_picture(fig2, Inches(6.8), Inches(1.5), Inches(5.6), Inches(4.2))

tx5 = s5.shapes.add_textbox(Inches(0.8), Inches(5.9), Inches(11.7), Inches(1.2))
p = tx5.text_frame.paragraphs[0]
p.text = "Left: As we added trees from 30 to 200, the error rate dropped steadily and stabilized at just 2.60% (97.40% OOB accuracy).\nRight: The top 3 diagnostic clues: HTTPS/SSL validity (29.3%), Anchor URL tags (23.5%), and Web Traffic volume (8.2%)."
p.font.size = Pt(14)
p.font.color.rgb = DARK_GRAY

# Slide 6: Master Performance Leaderboard (Confusion Matrix & ROC)
s6 = prs.slides.add_slide(blank_layout)
add_header(s6, "Champion Results: 97.42% Accuracy & 0.9943 ROC-AUC")
fig3 = os.path.join(FIG_DIR, "rf_confusion_matrix.png")
fig4 = os.path.join(FIG_DIR, "rf_roc_curve.png")

if os.path.exists(fig3):
    s6.shapes.add_picture(fig3, Inches(0.8), Inches(1.5), Inches(5.4), Inches(4.2))
if os.path.exists(fig4):
    s6.shapes.add_picture(fig4, Inches(6.8), Inches(1.5), Inches(5.4), Inches(4.2))

tx6 = s6.shapes.add_textbox(Inches(0.8), Inches(5.9), Inches(11.7), Inches(1.2))
p = tx6.text_frame.paragraphs[0]
p.text = "Left: Confusion matrix on 2,211 test URLs — 1,213 safe sites and 941 phishing sites correctly caught with only 19 missed (98.46% Recall).\nRight: ROC curve hugs the top-left corner with an AUC of 0.9943, proving near-perfect separation power."
p.font.size = Pt(14)
p.font.color.rgb = DARK_GRAY

# Slide 7: Speed & Computational Overhead (Group 1 Handover)
s7 = prs.slides.add_slide(blank_layout)
add_header(s7, "Blazing Speed: Ready for Real-Time Edge Deployment")
tx7 = s7.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.5))
tf7 = tx7.text_frame
tf7.word_wrap = True
add_bullet(tf7, "Training Speed", "Trained 150 deep decision trees across 8,843 training URLs in just 0.9793 seconds!")
add_bullet(tf7, "Ultra-Low Latency", "Classifying a single URL takes only 61.51 microseconds (0.0000615 seconds).")
add_bullet(tf7, "Real-World Throughput", "A standard single-core CPU can process over 16,000 URLs per second in real time.")
add_bullet(tf7, "Handover to Group 1 (Section 5.2)", "We exported all timing metrics into CSV and text summaries for Group 1's hardware latency report.")

# Slide 8: Multi-Group Collaboration (What We Gave Everyone)
s8 = prs.slides.add_slide(blank_layout)
add_header(s8, "CNS ISE Teamwork: Handover Packets for Groups 1 to 4")
tx8 = s8.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.5))
tf8 = tx8.text_frame
tf8.word_wrap = True
add_bullet(tf8, "To Group 1 (Latency Lead)", "Handed over training speed (0.98s) and single-sample latency (61.5 μs) for Section 5.2.")
add_bullet(tf8, "To Group 2 (Data Lead)", "Confirmed schema: 30 features, 80/20 stratified split, zero null values, target mapped for Section 3.1.")
add_bullet(tf8, "To Group 3 (Tournament Lead)", "Handed over Accuracy (97.42%), F1 (97.70%), Precision (96.96%), and Confusion Matrix for Section 5.1.")
add_bullet(tf8, "To Group 4 (System Setup Lead)", "Handed over exact Python 3.10.11, Scikit-learn 1.7.2, and Windows environment specs for Section 4.")

# Slide 9: Conclusion & Future Scope (Authored by Group 5)
s9 = prs.slides.add_slide(blank_layout)
add_header(s9, "Conclusion & What Comes Next (Section 6)")
tx9 = s9.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(11.7), Inches(5.5))
tf9 = tx9.text_frame
tf9.word_wrap = True
add_bullet(tf9, "Key Takeaway", "Hyper-tuned Random Forest delivers world-class phishing detection without needing to download malware payloads.")
add_bullet(tf9, "Real-World Browser Extension", "Our model is lightweight enough to be compiled into WebAssembly or ONNX and put directly inside Chrome/Brave.")
add_bullet(tf9, "Next Steps (Explainable AI)", "Add TreeSHAP so users can see exactly why a link was blocked (e.g. 'Blocked because SSL is fake and anchor tags point to unknown IP').")
add_bullet(tf9, "Continuous Learning", "Hook the model to live security feeds (PhishTank) to automatically adapt to new tricks every week.")

# Slide 10: Thank You Slide
s10 = prs.slides.add_slide(blank_layout)
bg10 = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
bg10.fill.solid()
bg10.fill.fore_color.rgb = NAVY
bg10.line.fill.background()

tx10 = s10.shapes.add_textbox(Inches(1.0), Inches(2.2), Inches(11.333), Inches(3.5))
tf10 = tx10.text_frame
tf10.word_wrap = True

p = tf10.paragraphs[0]
p.alignment = PP_ALIGN.CENTER
p.text = "Thank You! Any Questions?"
p.font.size = Pt(40)
p.font.bold = True
p.font.color.rgb = WHITE
p.space_after = Pt(20)

p2 = tf10.add_paragraph()
p2.alignment = PP_ALIGN.CENTER
p2.text = "CNS ISE — Group 5 Research Consortium\nAccuracy: 97.42% | Latency: 61.5 μs | Model: Random Forest Ensemble"
p2.font.size = Pt(20)
p2.font.color.rgb = TEAL

prs.save(PPTX_PATH)
print(f"[SUCCESS] Saved PPTX presentation to: {PPTX_PATH}")
