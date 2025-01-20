import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from common import StudentInfo, CourseInfo

ADVISOR_NAME = "Juncheng Yang"


def update():
    url_student = "https://junchengyang.com"

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

    course_info = {"Juncheng Yang": []}

    # student
    response = requests.get(url_student)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch the website {url_student}")
    data = str(response.content)
    pattern = r"<!--.*?-->"
    cleaned_html = re.sub(pattern, "", data, flags=re.DOTALL)

    soup = BeautifulSoup(cleaned_html, "html.parser")
    div = soup.find_all("div", id="student")[0]
    for id, degree in [
        ("postdoc", "Researcher & Postdoc"),
        ("phd", "Ph.D."),
        ("undergraduate", "Master & Undergraduate"),
    ]:
        div2 = div.find_all("div", id=id)
        if not div2:
            continue
        if not div2[0].select("ul"):
            continue
        for li in div2[0].select("ul")[0].find_all("li"):
            li_str = li.text.replace("\\n", "").strip()
            if "(" in li_str:
                name = li_str[: li_str.find("(")]
                note = li_str[li_str.find("(") + 1 : li_str.find(")")]
            else:
                name = li_str
                note = ""
            if li.a:
                url = urljoin(url_student, li.a["href"])
            else:
                url = ""

            student_info[degree].append(
                StudentInfo(name, degree, ADVISOR_NAME, url=url, note=note)
            )

    div = soup.find_all("div", id="alumni")[0]
    for id, degree in [
        ("postdoc", "Researcher & Postdoc"),
        ("phd", "Ph.D."),
        ("undergraduate", "Master & Undergraduate"),
    ]:
        div2 = div.find_all("div", id=id)
        if not div2:
            continue
        if not div2[0].select("ul"):
            continue
        for li in div2[0].select("ul")[0].find_all("li"):
            li_str = li.text.replace("\\n", "").strip()
            if "(" in li_str:
                name = li_str[: li_str.find("(")]
                note = li_str[li_str.find("(") + 1 : li_str.find(")")]
            else:
                name = li_str
                note = ""
            if li.a:
                url = urljoin(url_student, li.a["href"])
            else:
                url = ""

            alumni_info[degree].append(StudentInfo(name, degree, ADVISOR_NAME, url=url))
            
    div = soup.find_all("div", id="teaching")[0]
    for li in div.select("ul")[0].find_all("li"):
        s = str(li)
        course_num = " ".join(s.split()[:2])
        course_name = " ".join(s.split(":")[0].split()[2:])
        url = urljoin(url_student, li.a["href"]) if li.a else ""
        course_info[ADVISOR_NAME].append(
            CourseInfo(
                course_number=course_num,
                course_name=course_name,
                instructor=ADVISOR_NAME,
                url=url,
            )
        )


    return student_info, alumni_info, course_info


if __name__ == "__main__":
    update()
