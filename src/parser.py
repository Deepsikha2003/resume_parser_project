import spacy
import re
import pdfplumber
import docx
import os
from collections import defaultdict

# Load the trained spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("SpaCy model 'en_core_web_sm' not found. Downloading...")
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    """
    Extracts text from a PDF file using pdfplumber.
    """
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
    except Exception as e:
        return f"Error extracting text from PDF: {e}"
    return text

def extract_text_from_docx(file_path):
    """
    Extracts text from a DOCX file.
    """
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        return f"Error extracting text from DOCX: {e}"
    return text

def extract_contact_info(text):
    """
    Extracts email and phone number from the text.
    """
    email = re.findall(r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.com", text)
    phone = re.findall(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)
    return {
        "email": email[0] if email else None,
        "phone": phone[0] if phone else None,
    }

def extract_skills(text):
    """
    Extracts a predefined list of skills from the text.
    """
    skills_list = [
        "python", "java", "c++", "javascript", "react", "angular", "node.js",
        "sql", "nosql", "aws", "azure", "gcp", "docker", "kubernetes",
        "machine learning", "data science", "nlp", "html", "css", "agile"
    ]
    extracted_skills = [skill for skill in skills_list if re.search(r'\b' + re.escape(skill) + r'\b', text.lower())]
    return extracted_skills

def extract_education(text):
    """
    Extracts education-related information using spaCy's NER.
    """
    doc = nlp(text)
    education = []
    for ent in doc.ents:
        if ent.label_ == "ORG":
            # Simple heuristic for identifying universities/colleges
            if any(word in ent.text.lower() for word in ["university", "college", "institute", "school"]):
                education.append(ent.text)
    return education

def parse_resume(file_path):
    """
    Main function to parse a resume file.
    """
    if file_path.endswith('.pdf'):
        resume_text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        resume_text = extract_text_from_docx(file_path)
    else:
        return {"error": "Unsupported file type. Please upload a PDF or DOCX file."}

    if "Error" in resume_text:
        return {"error": resume_text}

    # Use the loaded nlp model to process the text
    doc = nlp(resume_text)
    name = doc.ents[0].text if doc.ents else None

    # Use the extraction functions
    contact_info = extract_contact_info(resume_text)
    skills = extract_skills(resume_text)
    education = extract_education(resume_text)

    return {
        "name": name,
        "contact_info": contact_info,
        "skills": skills,
        "education": education,
        "raw_text": resume_text
    }

if __name__ == "__main__":
    # Example usage for direct testing
    test_resume_path = "data/raw_resumes/resume1.pdf"
    if os.path.exists(test_resume_path):
        parsed_data = parse_resume(test_resume_path)
        print(parsed_data)
    else:
        print(f"Test file not found: {test_resume_path}")