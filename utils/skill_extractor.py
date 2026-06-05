def extract_skills(text):

    skills_db = [
        "python",
        "java",
        "c++",
        "sql",
        "mysql",
        "flask",
        "django",
        "git",
        "github",
        "docker",
        "kubernetes",
        "aws",
        "gcp",
        "html",
        "css",
        "javascript",
        "react",
        "mongodb"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills