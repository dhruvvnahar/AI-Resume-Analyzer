import os
from flask import Flask, render_template, request

from utils.pdf_parser import extract_text
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats
from ai.gemini_analyzer import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        # Check if file exists
        if "resume" not in request.files:
            return "No file uploaded"

        file = request.files["resume"]

        if file.filename == "":
            return "No file selected"

        # Save uploaded file
        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(filepath)

        # Extract text from PDF
        resume_text = extract_text(filepath)

        # Extract skills
        skills = extract_skills(resume_text)

        # Calculate ATS score
        ats_score = calculate_ats(skills)

        ai_analysis = analyze_resume(resume_text)

        # Generate HTML output
        return f"""
<html>
<head>
    <title>AI Resume Analyzer</title>
</head>

<body>

    <h1>AI Resume Analyzer</h1>

    <h2>ATS Score: {ats_score}%</h2>

    <h3>Skills Found</h3>

    <ul>
        {''.join([f'<li>{skill}</li>' for skill in skills])}
    </ul>

    <hr>

    <h2>AI Analysis</h2>

    <pre>{ai_analysis}</pre>

    <hr>

    <h3>Resume Preview</h3>

    <pre>{resume_text[:2000]}</pre>

    <br>

    <a href="/">Analyze Another Resume</a>

</body>
</html>
"""
