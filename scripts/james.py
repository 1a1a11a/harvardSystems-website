import json
from common import StudentInfo, CourseInfo


def update():
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
        "James Mickens": [
            CourseInfo(
                course_number="CS 263",
                course_name="Systems Security",
                instructor="James Mickens",
            )
        ]
    }

    return student_info, alumni_info, course_info


if __name__ == "__main__":
    update()
