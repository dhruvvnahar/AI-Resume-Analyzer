# AI Resume Analyzer

An AI-powered Resume Analyzer built using Python, Flask, and Google Gemini AI.

## Features

* Upload Resume PDF
* Extract Resume Text
* Detect Technical Skills
* Calculate ATS Score
* AI-Powered Resume Analysis
* Identify Strengths & Weaknesses
* Generate Improvement Suggestions

## Tech Stack

* Python
* Flask
* Google Gemini AI
* PyMuPDF
* HTML
* Bootstrap
* Jinja2

## Project Workflow

Resume Upload → PDF Parsing → Skill Extraction → ATS Scoring → Gemini AI Analysis → Result Dashboard

## Folder Structure

AI_Resume_Analyser/
├── app.py
├── requirements.txt
├── ai/
├── utils/
├── templates/
├── uploads/
└── README.md

## Installation

1. Clone the repository

git clone https://github.com/dhruvvnahar/AI-Resume-Analyzer.git

2. Navigate to the project folder

cd AI-Resume-Analyzer

3. Create virtual environment

python -m venv venv

4. Activate virtual environment

venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

6. Create a .env file

GEMINI_API_KEY=YOUR_API_KEY

7. Run the application

python app.py

## Future Enhancements

* Resume vs Job Description Matching
* PDF Report Generation
* Docker Support
* Google Cloud Deployment

## Author

Dhruv Nahar
