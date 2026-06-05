import os
from flask import Flask, render_template, request

from utils.pdf_parser import extract_text
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats
from ai.gemini_analyzer import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        # Check file uploaded
        if "resume" not in request.files:
            return "No file uploaded"

        file = request.files["resume"]

        if file.filename == "":
            return "No file selected"

        # Save file
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

        # Gemini Analysis
        ai_analysis = analyze_resume(resume_text)

        # Send data to result.html
        return render_template(
            "result.html",
            ats_score=ats_score,
            skills=skills,
            ai_analysis=ai_analysis,
            resume_text=resume_text
        )

    # First page load
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)