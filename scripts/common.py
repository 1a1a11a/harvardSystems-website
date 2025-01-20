
from dataclasses import dataclass, asdict

@dataclass
class StudentInfo:
    name: str
    position: str
    advisor: str
    email: str = ""
    research: str = ""
    photo: str = ""
    url: str = ""
    year: str = ""
    graduation_placement: str = ""
    note: str = ""

    def html(self):
        s = f'<li> <a href="{self.url}">{self.name}</a> '
        if self.note:
            s += f" (advised by {self.advisor}, {self.note})"
        else:
            s += f" (advised by {self.advisor})"
        s += "</li>"
        return s
    
@dataclass
class CourseInfo:
    course_number: str
    course_name: str
    instructor: str
    course_description: str = ""
    semester: str = ""
    year: str = ""
    course_url: str = ""

    def html(self):
        return f"""<li> <a href="{self.course_url}">{self.course_number}: {self.course_name}</a> </li>"""
