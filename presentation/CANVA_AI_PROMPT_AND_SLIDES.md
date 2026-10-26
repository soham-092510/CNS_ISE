# Group 5: Canva AI Prompts, Presentation Script & Simple Project Guide

> **Project Title:** Heuristic URL Feature Profiling for Phishing Domain Spotting Using Hyper-Tuned Random Forest Ensembles  
> **Coursework:** Cryptography and Network Security (CNS ISE) — Group 5  
> **Pre-Generated PowerPoint File:** [`presentation/Group5_Presentation.pptx`](file:///c:/Users/HP/OneDrive/Documents/Soham/Projects/CNS%20ISE/presentation/Group5_Presentation.pptx)  

---

## 🎨 1. The Exact Canva AI Prompt (Copy & Paste this into Canva Magic Design)

Open [Canva](https://www.canva.com/) -> Click **Create a Design** -> Select **Presentation (16:9)** -> Open **Magic Design / AI Presentation Maker**, and paste this exact prompt:

```text
Create a modern, clean, cybersecurity-themed 10-slide academic presentation with a deep navy blue, cyan, and white color palette.

Title: Heuristic URL Feature Profiling for Phishing Domain Spotting Using Hyper-Tuned Random Forest Ensembles (Group 5 - CNS ISE).

Slide Structure:
Slide 1: Title Slide with academic theme and subtitle "Detecting Fake Websites in Microseconds with 97.42% Accuracy".
Slide 2: "The Phishing Problem" - Explain why Google blacklists fail against modern fake websites (short-lived domains active for only 4 hours).
Slide 3: "Our Approach: URL Heuristic Profiling" - Checking 30 subtle clues in web addresses (like fake SSL, weird anchor tags, nested subdomains) without downloading malware.
Slide 4: "Why Random Forest?" - Use the simple analogy of a committee of 150 digital detectives voting democratically to eliminate individual mistakes.
Slide 5: "Dataset & Methodology" - Kaggle 11,054 verified URLs, 80/20 train-test split, zero missing values, 5-fold cross-validation.
Slide 6: "Out-of-Bag (OOB) Convergence" - How the error rate steadily dropped to just 2.60% as we scaled from 30 to 200 trees.
Slide 7: "What Clues Matter Most?" - Ranking the top structural URL features (HTTPS validation 29.3%, Anchor URL ratio 23.5%, Website Traffic 8.2%).
Slide 8: "Champion Results & Confusion Matrix" - Highlighting 97.42% Accuracy, 98.46% Recall, 97.70% F1-score, and 0.9943 ROC-AUC.
Slide 9: "Blazing Speed for Real-Time Edge Filtering" - 0.98s training time, 61.5 microseconds per URL, over 16,000 URLs processed per second.
Slide 10: "Conclusion & Future Work" - Building browser extensions and explainable AI (TreeSHAP). Thank you & Q&A.

Style: Clean typography, high-contrast badges, cards, data metrics callouts, and minimal clutter.
```

---

## 🧠 2. "Explain Like I'm 5" — What Did We Actually Do?
*(Read this once, and you will understand the entire project 100%!)*

1. **What is Phishing?**
   - Hackers create fake websites that look identical to real ones (like `paypa1-security-login.xyz` instead of `paypal.com`) to steal passwords and credit cards.

2. **Why can't Google just blacklist them?**
   - Traditional security uses "Blacklists" (lists of known bad sites). But hackers create a fake site in 5 minutes, attack people, and delete the site after 4 hours. By the time Google adds it to a blacklist, the damage is already done!

3. **What is our solution?**
   - Instead of waiting for a website to be reported, we inspect the **URL address itself**!
   - We look at **30 subtle clues** (called *heuristics*):
     - Does it use an IP address instead of a domain name?
     - Does it have 5 subdomains like `apple.com.secure-id.auth-check.xyz`?
     - Is the HTTPS certificate fake or expired?
     - Do the buttons on the page point to external hacker servers?
   - And the best part: We check all this **without downloading or running the web page**, so your computer never gets infected.

4. **What is Random Forest (Our Model)?**
   - Think of a single Decision Tree like **one detective**. One detective might miss a clue or be tricked.
   - **Random Forest is a committee of 150 independent detectives!**
   - Each detective is trained on a different random bundle of data and looks at different clues.
   - When a new URL comes in, all 150 detectives vote: *Is it fake or safe?* If 145 say fake, it's blocked!
   - This democratic voting is why our model almost never makes mistakes.

5. **Our Numbers (The Flex):**
   - We tested on **11,054 real websites** from Kaggle.
   - **Accuracy: 97.42%** (caught almost everything).
   - **Recall: 98.46%** (out of 100 phishing sites, we catch over 98!).
   - **Speed: 61.5 microseconds** (that's 0.00006 seconds per link — fast enough to scan 16,000 URLs every single second).

---

## 🎤 3. Slide-by-Slide Script (What to Show & What to Say)

### Slide 1: Title Slide
- **Title:** Heuristic URL Feature Profiling for Phishing Domain Spotting Using Hyper-Tuned Random Forest Ensembles
- **Subtitle:** CNS ISE Project — Group 5
- **What to say:**
  > *"Good morning professors and fellow students. Today, Group 5 presents our machine learning research on detecting phishing websites using Random Forest ensembles and URL heuristic profiling."*

---

### Slide 2: The Real-World Problem
- **Key Points:**
  - Phishing causes billions of dollars in losses every year.
  - Blacklists are too slow: Zero-day phishing campaigns only last 4 to 8 hours.
  - Users click before blacklists update.
- **What to say:**
  > *"The fundamental problem in cybersecurity today is speed. Blacklists like Google Safe Browsing only work after a domain is reported. But modern phishing attacks are ephemeral — attackers launch a site, steal credentials within four hours, and shut it down. We need an automated perimeter system that spots fake domains in real time before a user even opens the page."*

---

### Slide 3: Our Solution — 30 URL Clues
- **Key Points:**
  - Zero payload download needed (100% safe).
  - 30 discrete heuristic markers (IP in URL, @ symbol, hyphenation, subdomain depth, SSL certificate trust, Alexa traffic).
- **What to say:**
  > *"Instead of rendering dangerous JavaScript on the client machine, our approach extracts 30 lightweight heuristic features directly from the URL string. These include lexical patterns like prefix-suffix hyphens, structural signals like subdomain count, and network reputation signals like domain registration length."*

---

### Slide 4: Why Random Forest?
- **Key Points:**
  - Ensemble of 150 decision trees.
  - Bootstrap aggregation (Bagging) reduces variance without increasing bias.
  - Random feature projection ($m = \sqrt{30} \approx 5$ clues per split).
  - Out-of-Bag (OOB) error for built-in cross-validation.
- **What to say:**
  > *"Our assigned algorithm for Group 5 is the Random Forest Classifier. Instead of relying on a single complex decision boundary, Random Forest builds 150 distinct trees using bootstrap sampling and random feature projection. The ensemble aggregates their predictions through majority voting, making it extraordinarily resilient against obfuscation."*

---

### Slide 5: Experimental Convergence — Out-of-Bag (OOB) Curve
- **Image to Insert:** `figures/rf_oob_error_decline.png`
- **Key Points:**
  - Tested tree counts from 30 up to 200 trees.
  - OOB error dropped steeply and stabilized at **2.60% (97.40% OOB accuracy)** at 130 trees.
- **What to say:**
  > *"This slide illustrates our Out-of-Bag error tracking plot. As we scaled from 30 to 200 estimators, the internal generalization error declined asymptotically and plateaued at just 2.60% around 130 to 150 trees, confirming that the forest achieves maximum stability without overfitting."*

---

### Slide 6: What URL Features Matter Most? (MDI Ranking)
- **Image to Insert:** `figures/rf_top10_features.png`
- **Key Points:**
  - #1: **HTTPS / SSL Trust (29.32%)**
  - #2: **Anchor URL Discrepancies (23.45%)**
  - #3: **Global Web Traffic (8.19%)**
  - #4: **Subdomain Depth (6.66%)**
  - #5: **Hyphenated Prefix-Suffix (4.62%)**
- **What to say:**
  > *"We extracted the Mean Decrease in Gini Impurity to understand what clues the model relies upon. As shown in the chart, the top two indicators are SSL certificate status at 29.3% and anchor URL ratio at 23.5%. Fake websites almost always fail proper SSL certificate validation or use mismatched hyperlink anchor targets."*

---

### Slide 7: Champion Results & Confusion Matrix
- **Image to Insert:** `figures/rf_confusion_matrix.png` and `figures/rf_roc_curve.png`
- **Key Points:**
  - **97.42% Accuracy** on 2,211 held-out test URLs.
  - **98.46% Recall** (Sensitivity) — catches 98 out of 100 attacks.
  - **0.9943 ROC-AUC** score.
  - Only 19 false negatives out of 2,211 samples.
- **What to say:**
  > *"On our held-out test set of 2,211 URLs, the hyper-tuned Random Forest achieved 97.42% accuracy and 98.46% recall, with an Area Under the ROC Curve of 0.9943. In cybersecurity, recall is critical: our model missed only 19 phishing websites out of thousands."*

---

### Slide 8: Computational Latency & Edge Viability
- **Key Points:**
  - Training speed: **0.98 seconds** for 8,843 samples.
  - Inference latency: **61.51 microseconds** per URL.
  - Throughput: Over **16,000 URLs evaluated per second** per CPU core.
  - Handed over to Group 1 for Section 5.2.
- **What to say:**
  > *"High accuracy is useless if a filter slows down web browsing. Our latency analysis shows that the model takes only 61.5 microseconds to evaluate a URL. A single standard processor core can inspect over 16,000 URLs per second, making this architecture suitable for edge routers, enterprise proxies, and browser extensions."*

---

### Slide 9: Multi-Group Collaboration (Teamwork)
- **Key Points:**
  - Delivered Section 5.2 timing data to Group 1.
  - Confirmed 30-feature data pipeline with Group 2.
  - Submitted tournament metrics to Group 3 for Section 5.1 Leaderboard.
  - Provided hardware specs and library versions to Group 4.
  - Group 5 authored Section 1, Section 2 (2 Scopus papers), Section 3.5 (RF Math), and Section 6 (Conclusion).
- **What to say:**
  > *"This was an integrated multi-group project. Group 5 authored Sections 1, 2, 3.5, and 6, and successfully delivered all benchmark handovers to Groups 1 through 4."*

---

### Slide 10: Conclusion & Q&A
- **Key Points:**
  - Random Forest is fast, robust, and highly accurate for perimeter phishing defense.
  - Future scope: Client-side browser extension (Wasm/ONNX) and TreeSHAP explainability.
  - Open for Questions!
- **What to say:**
  > *"In conclusion, URL heuristic profiling with hyper-tuned Random Forest provides a lightweight, highly accurate, and non-intrusive defense against zero-day phishing domains. Thank you, and we welcome any questions!"*

---

## 🎯 4. Cheat-Sheet: Top 3 Viva / Professor Questions & 1-Line Answers

**Q1: Why did you pick Random Forest over a single Decision Tree?**  
*Answer:* *"A single decision tree easily overfits and has high variance. Random Forest builds 150 decorrelated trees via bagging and random feature selection, using majority voting to eliminate individual errors."*

**Q2: What is Out-of-Bag (OOB) error?**  
*Answer:* *"Because bootstrap sampling only picks about 63.2% of the training data for each tree, the remaining 36.8% of unused data acts as a free validation set to measure real generalization error without needing a separate holdout partition."*

**Q3: Which URL feature is the strongest indicator of phishing?**  
*Answer:* *"SSL/HTTPS validation (accounting for 29.32% of total Gini impurity reduction), closely followed by Anchor URL mismatch (23.45%)."*
