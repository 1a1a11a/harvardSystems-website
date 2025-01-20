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
        "Eddie Kohler": [
            CourseInfo(
                course_number="CS 161",
                course_name="Operating Systems",
                instructor="Eddie Kohler",
                course_url="https://read.seas.harvard.edu/cs161/2024/",
            ),
            CourseInfo(
                course_number="CS 61",
                course_name="Systems Programming and Machine Organization",
                instructor="Eddie Kohler",
                course_url="https://cs61.seas.harvard.edu/site/2024/",
            ),
            CourseInfo(
                course_number="CS 260r",
                course_name="Large-Scale Distributed and Parallel Computations",
                instructor="Eddie Kohler",
                semester="Spring 2022",
                year="2022",
                course_url="https://read.seas.harvard.edu/cs260r/2022/",
            ),
            CourseInfo(
                course_number="CS 260r",
                course_name="Serverless Computing",
                instructor="Eddie Kohler",
                semester="Spring 2019",
                year="2019",
                course_url="https://www.read.seas.harvard.edu/~kohler/class/cs260r-s19/",
            ),
            CourseInfo(
                course_number="CS 260r",
                course_name="Verified Systems",
                instructor="Eddie Kohler",
                semester="Spring 2017",
                year="2017",
                course_url="https://www.read.seas.harvard.edu/~kohler/class/cs260r-s17/",
            ),
            CourseInfo(
                course_number="CS 260r",
                course_name="Reliable Systems",
                instructor="Eddie Kohler",
                semester="Spring 2017",
                year="2017",
                course_url="https://www.read.seas.harvard.edu/~kohler/class/cs260r-s15/",
            ),
            CourseInfo(
                course_number="CS 260r",
                course_name="Cloud Big Data Systems",
                instructor="Eddie Kohler",
                semester="Spring 2017",
                year="2017",
                course_url="https://www.read.seas.harvard.edu/~kohler/class/cs260r-s14/",
            ),
            CourseInfo(
                course_number="CS 261",
                course_name="Research Topics in Operating Systems",
                instructor="Eddie Kohler",
                course_url="https://read.seas.harvard.edu/cs261/2021/",
            ),
            CourseInfo(
                course_number="CS 207",
                course_name="CS 207 Systems Development for Computational Science",
                instructor="Eddie Kohler",
                course_url="https://www.read.seas.harvard.edu/~kohler/class/cs207-s12/",
            ),
        ]
    }

    return student_info, alumni_info, course_info


if __name__ == "__main__":
    update()
