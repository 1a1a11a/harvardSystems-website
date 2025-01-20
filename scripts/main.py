import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__)))
from minlan import update as minlan_update
from eddie import update as eddie_update
from james import update as james_update
from stratos import update as stratos_update
from juncheng import update as juncheng_update

UPDATE_FUNCS = [
    minlan_update,
    eddie_update,
    james_update,
    stratos_update,
    juncheng_update,
]


def add_student_and_course():
    html_code_student = {
        "Researcher & Postdoc": "<h5> Researcher & Postdoc </h5>\n<ul>",
        "Ph.D.": "<h5> Ph.D. students </h5>\n<ul>",
        "Master & Undergraduate": "<h5> Master & Undergraduate </h5>\n<ul>",
    }
    html_code_alumni = {
        "Researcher & Postdoc": "<h5> Researcher & Postdoc </h5>\n<ul>",
        "Ph.D.": "<h5> Ph.D. students </h5>\n<ul>",
        "Master & Undergraduate": "<h5> Master & Undergraduate </h5>\n<ul>",
    }
    html_code_course = ""

    courses = set()
    students = set()
    for update_func in UPDATE_FUNCS:
        student_info, alumni_info, course_info = update_func()
        for key in student_info:
            for student in student_info[key]:
                if student.name in students:
                    continue
                html_code_student[key] += student.html() + "\n"
                students.add(student.name)
        for key in alumni_info:
            for alumni in alumni_info[key]:
                if alumni.name in students:
                    continue
                html_code_alumni[key] += alumni.html() + "\n"
                students.add(alumni.name)
        for course_list in course_info.values():
            for course in course_list:
                if course.course_name in courses:
                    continue
                html_code_course += course.html() + "\n"
                courses.add(course.course_name)

    html = open("index_base.html").read()
    html = html.replace(
        "<!-- student_info -->",
        html_code_student["Researcher & Postdoc"]
        + "\n</ul>\n"
        + html_code_student["Ph.D."]
        + "\n</ul>\n"
        + html_code_student["Master & Undergraduate"]
        + "\n</ul>",
    )

    html = html.replace(
        "<!-- alumni_info -->",
        html_code_alumni["Researcher & Postdoc"]
        + "\n</ul>\n"
        + html_code_alumni["Ph.D."]
        + "\n</ul>\n"
        + html_code_alumni["Master & Undergraduate"]
        + "\n</ul>",
    )

    html = html.replace("<!-- course_info -->", html_code_course + "\n</ul>")
    with open("index.html", "w") as f:
        f.write(html)


def add_sponsor():
    html_code_sponsor = ""
    for f in os.listdir("img/sponsor"):
        html_code_sponsor += f'<img class="col-1 m-1 mb-2" src="img/sponsor/{f}" alt="{f}" style="max-height: 48px; width: auto;">\n'
    html = open("index.html").read()
    html = html.replace(
        "<!-- sponsor_info -->",
        html_code_sponsor,
    )
    with open("index.html", "w") as f:
        f.write(html)


def update_time():
    import time

    html = open("index.html").read()
    html = html.replace(
        "<!-- update_time -->",
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    )
    with open("index.html", "w") as f:
        f.write(html)


def run():
    add_student_and_course()
    add_sponsor()

    update_time()


if __name__ == "__main__":
    run()
