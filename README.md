# 📄 ATS Resume Screening Bot with Python & NLP

## 🧩 Overview  
This project simulates how an **Applicant Tracking System (ATS)** screens resumes against a job description. It extracts keywords from both documents, computes **TF-IDF vector similarity**, and highlights missing skills, generating a shortlist decision with a transparent scoring breakdown.

## 🎯 Project Objective

- **Initial Goal**: Automate the process of matching resumes to job descriptions using a scoring-based approach.
- **Final Outcome**: Built a robust Python tool that evaluates resumes using NLP-based similarity metrics and keyword overlap to predict “Shortlisted” or “Not Shortlisted” status.

## 🗂️ Dataset & Inputs

The inputs are:
- 📄 `job_description.txt`: Contains the full job description text.
- 📂 `resumes/`: A folder containing `.pdf` or `.txt` files of applicant resumes.

Each resume is processed and compared against the job description for:
- **TF-IDF Similarity**
- **Keyword Match Rate**
- **Final ATS Score** (Weighted combination)

## 🛠️ Technologies Used

- **Python**
- **PyPDF2** – PDF text extraction
- **scikit-learn** – TF-IDF vectorization and cosine similarity
- **NumPy, pandas** – Data handling
- **Regex** – Basic keyword extraction
- *(Optional)*: `pdfplumber` for more accurate PDF parsing

## 🚀 How to Run

### ⚙️ Script Mode (No GUI)
1. **Clone the Repository & Install Requirements**
```bash
pip install PyPDF2 scikit-learn pandas numpy
```

2. **Place Your Files**
```
project/
├── resume_screening_bot.py
├── job_description.txt
└── resumes/
    ├── resume1.pdf
    └── resume2.txt
```

3. **Run the Script**
```bash
python resume_screening_bot.py
```

4. **Output**
- Console: Similarity score, keyword match score, ATS score, decision
- CSV: `screened_resumes.csv` with all results and missing keywords

## 🔁 Workflow

### 1. Text Extraction
- PDFs are parsed using `PyPDF2` or `pdfplumber`
- Text is cleaned and normalized

### 2. Keyword Extraction
- Noun-like terms are extracted from job description and resume
- Common stopwords are removed

### 3. Scoring Logic
- **TF-IDF Vector Similarity** (60% weight)
- **Keyword Match Ratio** (40% weight)
- Final ATS Score = 0.6 × Similarity + 0.4 × Keyword Match
- Threshold = 0.35 for shortlisting

### 4. Output
- Each resume gets:  
  - Similarity Score  
  - Keyword Match Score  
  - Final ATS Score  
  - ✅ “Shortlisted” or ❌ “Not Shortlisted”  
  - Top missing keywords

## 📊 Results
Sample result for `sample_resume.pdf`:

| Resume             | Similarity | Keyword Match | ATS Score | Decision        |
|--------------------|------------|----------------|------------|------------------|
| sample_resume.pdf | 0.74       | 0.65           | 0.703      | ✅ Shortlisted   |

## 🔍 Feature Importance

### Contributing Features:
- ✅ **Relevant technical skills** (Python, ML, SQL)
- ✅ **Matching academic background** (Data Science-related)
- ✅ **Project-based keywords** (A/B testing, modeling, dashboards)

### Missing Keywords (if any):
- `postgresql`, `qlik`, `telehealth`, etc. *(example)*

## 💡 Key Takeaways

- Combining **TF-IDF** with **keyword overlap** yields more transparent screening logic than black-box LLMs.
- Academic + internship resumes can pass ATS when aligned with job wording.
- The tool highlights what’s missing — guiding targeted resume improvement.

## 📈 Future Enhancements

- Add support for scoring cover letters alongside resumes  
- Integrate Named Entity Recognition (NER) to extract structured info  
- Export PDF report with scores and improvement tips  
- Streamlit web app interface for drag-and-drop scoring  
- Multilingual JD + resume screening  
- Parse LinkedIn profile URLs directly via scraping
