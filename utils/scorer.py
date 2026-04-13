# utils/scorer.py
def calculate_score(resume_skills, job_skills):
    matched = set(resume_skills) & set(job_skills)
    score = (len(matched) / len(job_skills)) * 100
    return round(score, 2)

