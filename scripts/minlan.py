import requests
import json
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from common import StudentInfo, CourseInfo

ADVISOR_NAME = "Minlan Yu"


def update():
    url_student = "https://minlanyu.seas.harvard.edu/student.html"
    url_course = "https://minlanyu.seas.harvard.edu/teach.html"

    student_info = {
        "Researcher & Postdoc": [],
        "Ph.D.": [],
        "Master & Undergraduate": [],
    }
    alumni_info = {
        "Researcher & Postdoc": [],
        "Ph.D.": [],
        "Master & Undergraduate": [],
    }

    course_info = {ADVISOR_NAME: []}

    # student
    response = requests.get(url_student)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch the website {url_student}")

    soup = BeautifulSoup(response.content, "html.parser")

    # current student
    for position, ul_idx, info_list in (
        ("Ph.D.", "4", student_info["Ph.D."]),
        ("Postdoc", "6", student_info["Researcher & Postdoc"]),
        ("Ph.D.", "8", alumni_info["Ph.D."]),
        ("Postdoc", "10", alumni_info["Researcher & Postdoc"]),
        ("Undergraduate", "13", alumni_info["Master & Undergraduate"]),
    ):
        ul = soup.select(f"body > div > div > ul:nth-child({ul_idx})")[0]
        for li in ul.select("li"):
            name = li.text.strip()
            note = ""
            if "(" in name:
                note = name[name.index("(") + 1 : name.rindex(")")]
                name = name[: name.index("(")]

            student = StudentInfo(
                name=name.strip(),
                position=position,
                url=urljoin(url_student, li.a["href"]) if li.a else "",
                note=note.strip(),
                advisor=ADVISOR_NAME,
            )
            info_list.append(student)

    # course
    response = requests.get(url_course)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch the website {url_course}")

    course_soup = BeautifulSoup(response.content, "html.parser")
    ul = course_soup.select("body > div > div > ul")[0]
    for li in ul.select("li"):

        course_num_and_name = li.text.split(":")[1].strip()
        s = course_num_and_name.split(" ")
        if s[0] != "CS":
            continue
        if s[1] == "61":
            continue
        course = CourseInfo(
            course_number=" ".join(s[:2]),
            course_name=" ".join(s[2:]),
            course_url=urljoin(url_course, li.a["href"]) if li.a else "",
            instructor=ADVISOR_NAME,
        )
        course_info[ADVISOR_NAME].append(course)

    return student_info, alumni_info, course_info


if __name__ == "__main__":
    update()
