import requests
import json
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from common import StudentInfo, CourseInfo


def update():
    url = "http://daslab.seas.harvard.edu/"

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

    course_info = {
        "Stratos Idreos": [
            CourseInfo(
                course_number="CS 165",
                course_name="Data Systems",
                instructor="Stratos Idreos",
            ),
            CourseInfo(
                course_number="CS 265",
                course_name="Big Data Systems",
                instructor="Stratos Idreos",
            ),
        ]
    }

    resp = requests.get(url)
    if resp.status_code != 200:
        raise RuntimeError(f"Failed to fetch the website {url}")
    data = str(resp.content)
    pattern = r"<!--.*?-->"
    cleaned_html = re.sub(pattern, "", data, flags=re.DOTALL)

    soup = BeautifulSoup(cleaned_html, "html.parser")

    # this is the alumni section
    div = soup.find_all("div", id="slide")[0]
    first_alum = div.find("div", class_="team-member")
    first_alum_name = first_alum.h4.text.replace("\\n", "").strip("\n ")

    current_sec = student_info
    for div in soup.find_all("div", class_="team-member"):
        url = ""
        if div.a and div.a.has_attr("href"):
            if len(div.a["href"]) > 8 and div.a["href"][0] != "#":
                url = div.a["href"]

        name = div.h4.text.replace("\\n", "").strip("\n ")
        if name == "Stratos Idreos":
            continue
        if name == first_alum_name:
            current_sec = alumni_info
        position = div.p.text.replace("\\n", "").strip().lower()
        if (
            "undergraduate" in position
            or "undergrad" in position
            or "graduate" in position
        ):
            position = "Master & Undergraduate"
        elif "ph.d." in position:
            position = "Ph.D."
        elif "Postdoc" in position:
            position = "Postdoc"
        elif "researcher" in position or "scholar" in position:
            position = "Researcher & Postdoc"
        else:
            if "research intern" in position:
                continue
            else:
                print(f'Unknown position: "{position}"')
                continue
        note = ""
        pos = position.find("next: ")
        if pos != -1:
            note = "Next: " + position[pos + 6 :].strip()

        photo = ""
        if div.img and div.img.has_attr("src"):
            photo = div.img["src"]

        student = StudentInfo(
            name=name,
            position=position,
            advisor="Stratos Idreos",
            url=url,
            photo=photo,
            note=note,
        )
        current_sec[position].append(student)

    return student_info, alumni_info, course_info


if __name__ == "__main__":
    update()
    # test()
