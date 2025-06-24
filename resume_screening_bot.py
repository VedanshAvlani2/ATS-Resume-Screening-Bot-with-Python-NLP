import os
import re
from PyPDF2 import PdfReader
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_pdf(filepath):
    with open(filepath, "rb") as f:
        reader = PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

def clean_text(text):
    return re.sub(r'\s+', ' ', text.lower())

def extract_keywords(text):
    # Simple keyword extraction using unique nouns/adjectives
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    stopwords = set([
        'with', 'that', 'from', 'this', 'have', 'will', 'you', 'your', 
        'for', 'and', 'the', 'are', 'our', 'but', 'has', 'was', 'any', 'who', 'not'
    ])
    return sorted(set(w for w in words if w not in stopwords))

def ats_score(jd_text, resume_text, threshold=0.35):
    # TF-IDF similarity
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([jd_text, resume_text])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

    # Keyword overlap
    jd_keywords = set(extract_keywords(jd_text))
    resume_keywords = set(extract_keywords(resume_text))
    match_count = len(jd_keywords & resume_keywords)
    missing = jd_keywords - resume_keywords
    match_score = match_count / max(len(jd_keywords), 1)

    final_score = (0.6 * similarity) + (0.4 * match_score)
    decision = "Shortlisted ✅" if final_score >= threshold else "Not Shortlisted ❌"

    return {
        "similarity": round(similarity, 3),
        "keyword_match": round(match_score, 3),
        "final_score": round(final_score, 3),
        "decision": decision,
        "missing_keywords": sorted(list(missing))[:10]  # top missing
    }

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Paths
    jd_path = "job_description.txt"
    resume_path = "C:\Users\vedan\OneDrive\Documents\Projects\30 day 30 projects\Day 1\resumes"  # Replace with path to your actual resume

    # Load files
    jd_text = clean_text(open(jd_path, encoding='utf-8').read())
    resume_text = clean_text(extract_text_from_pdf(resume_path))

    # Score
    result = ats_score(jd_text, resume_text)

    # Display result
    print("\n--- ATS Resume Screening Result ---")
    print(f"Similarity Score      : {result['similarity']}")
    print(f"Keyword Match Score   : {result['keyword_match']}")
    print(f"Final ATS Score       : {result['final_score']}")
    print(f"Decision              : {result['decision']}")
    print(f"Missing Keywords      : {', '.join(result['missing_keywords'])}")
