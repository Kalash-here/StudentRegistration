import unittest
from pathlib import Path
from html.parser import HTMLParser


class FormParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = set()
        self.input_names = set()
        self.button_types = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append(tag)

        if "id" in attrs:
            self.ids.add(attrs["id"])

        if tag == "input" and "name" in attrs:
            self.input_names.add(attrs["name"])

        if tag == "button":
            self.button_types.add(attrs.get("type", ""))


class TestStudentRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        path = Path(__file__).parent / "index.html"
        cls.html = path.read_text(encoding="utf-8")

        cls.parser = FormParser()
        cls.parser.feed(cls.html)

    def test_registration_form_exists(self):
        self.assertIn("form", self.parser.tags)
        self.assertIn("studentRegistration", self.parser.ids)

    def test_student_name_exists(self):
        self.assertIn("studentName", self.parser.input_names)

    def test_roll_number_exists(self):
        self.assertIn("rollNumber", self.parser.input_names)

    def test_email_exists(self):
        self.assertIn("email", self.parser.input_names)

    def test_course_exists(self):
        self.assertIn('id="course"', self.html)

    def test_submit_button_exists(self):
        self.assertIn("submit", self.parser.button_types)


if __name__ == "__main__":
    unittest.main()