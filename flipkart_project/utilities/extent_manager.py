# utilities/extent_manager.py

from datetime import datetime
from pytest_html import extras


class ExtentManager:
    _instance = None

    def __init__(self):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.report_name = f"Reports/Flipkart_{timestamp}.html"

    @staticmethod
    def get_instance():
        if not ExtentManager._instance:
            ExtentManager._instance = ExtentManager()
        return ExtentManager._instance

    def create_test(self, test_name):
        print(f"Running Test: {test_name}")
        return self

    def log(self, status, message):
        print(f"[{status}] {message}")

    def flush(self):
        print("Report flushed successfully.")
