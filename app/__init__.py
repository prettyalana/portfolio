import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

mapbox_api_key = os.getenv("MAPBOX_API_KEY")
url=os.getenv("URL")

@app.route("/")
def index():
    pages = [
    {"name": "Home", "url": "/"},
    {"name": "About", "url": "/#about-me"},
    {"name": "Experience", "url": "/#work-experience"},
    {"name": "Hobbies", "url": "/hobbies"},
    {"name": "Education", "url": "/#education"},
    {"name": "Map", "url": "/#map"},
]
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

    education = [
        {
            "name_and_location": "Illinois Institute of Technology Stuart School of Business, Chicago, IL"
        },
        {
            "name_and_location": "University of Illinois - Discovery Partners Institute Tech Apprenticeship, Chicago, IL",
            "additional_information": [
                {
                    "degree_or_certificate": "Certificate of Completion Software Development",
                    "course_work": "Relevant coursework: Software Engineering",
                }
            ],
        },
    ]

    hobbies = [
        {
            "image": "https://images.pexels.com/photos/4792079/pexels-photo-4792079.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            "card_text": "Crocheting",
        },
        {
            "image": "https://images.unsplash.com/photo-1562232573-0305012a8818?q=80&w=3024&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "card_text": "Reading",
        },
        {
            "image": "https://images.pexels.com/photos/5187650/pexels-photo-5187650.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            "card_text": "Shopping",
        },
        {
            "image": "http://127.0.0.1:5000/static/img/batu-gezer-1HcNgs3RrKE-unsplash-200x200.jpg",
            "card_text": "Gaming",
        },
        {
            "image": "https://images.unsplash.com/photo-1661894782790-d1143da4f2f5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "card_text": "Traveling and Foreign Languages",
        },
    ]

    return render_template(
        "index.html",
        work_history=work_history,
        education=education,
        hobbies=hobbies,
        title="Alana",
        url=url,
        mapbox_api_key=mapbox_api_key,
        pages=pages
    )


@app.route("/hobbies")
def hobbies():
    hobbies_list = [
        {
            "image": "https://images.pexels.com/photos/4792079/pexels-photo-4792079.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            "card_text": "Crocheting",
        },
        {
            "image": "https://images.unsplash.com/photo-1562232573-0305012a8818?q=80&w=3024&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "card_text": "Reading",
        },
        {
            "image": "https://images.pexels.com/photos/5187650/pexels-photo-5187650.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
            "card_text": "Shopping",
        },
        {
            "image": "http://127.0.0.1:5000/static/img/batu-gezer-1HcNgs3RrKE-unsplash-200x200.jpg",
            "card_text": "Gaming",
        },
        {
            "image": "https://images.unsplash.com/photo-1661894782790-d1143da4f2f5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "card_text": "Traveling and Foreign Languages",
        },
    ]

    return render_template(
        "hobbies.html",
        hobbies=hobbies_list,
        title="Alana",
        url=url
    )
