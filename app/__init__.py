import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route("/")
def index():
    # array of dictionaries 
    work_history = [
        {
            "company": "Build Carolina Academy",
            "role_and_dates": "Teaching Assistant, Remote — April 2025 to Present",
            "job_functions": [
                "Assist 7 students in a 20-week part-time coding bootcamp with assignments and technical challenges, providing one-on-one and small group support",
                "Address student questions, escalating unresolved issues to the instructor or relevant staff",
                "Foster collaboration by connecting students with similar challenges and guiding peer-to-peer problem solving",
                "Collaborate with the instructor to develop and review content, ensuring all materials are approved prior to distribution",
            ],
        },
        {
            "company": "Everyone Can Code Chicago",
            "role_and_dates": "iOS App Developer Intern, Chicago, IL — June 2024 to August 2024",
            "job_functions": [
                "Gained foundational knowledge of the Swift programming language, enhancing coding proficiency for future impactful iOS development projects",
                "Collaborated with a team of 3 developers to design, build, and implement functional app features",
                "Utilized Figma to create a wireframe and designed a Storyboard for early app ideas",
                "Delivered a Minimum Viable Product (MVP) pitch to Apple executives",
                "Employed Git version control to manage source code changes in a team-based environment",
                "Built interactive user interfaces and custom views with SwiftUI and MapKit",
            ],
        },
        {
            "company": "Discovery Partners Institute",
            "role_and_dates": "Software Developer Apprentice, Chicago, IL — February 2024 to May 2024",
            "job_functions": [
                "Developed scalable full-stack applications using Ruby on Rails and PostgreSQL, applying object-oriented programming principles and a problem-first approach",
                "Executed weekly sprint deliverables in an agile environment, participating in daily stand-ups and retrospectives",
                "Implemented front-end features with HTML, CSS, and jQuery, ensuring responsive and user-friendly interfaces",
                "Utilized AWS for image storage, enhancing application functionality and performance",
                "Wrote clean, maintainable code by following industry best practices",
                "Managed Git repositories, including branching, merging, and pull requests both independently and in team-based challenges",
            ],
        },
    ]
    return render_template("index.html", work_history=work_history, title="Alana", url=os.getenv("URL"))
