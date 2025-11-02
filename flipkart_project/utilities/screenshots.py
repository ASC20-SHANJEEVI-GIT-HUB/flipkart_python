# utilities/screenshots.py

import os
from datetime import datetime


class Screenshots:
    @staticmethod
    def capture(driver, test_name):
        os.makedirs("Screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filepath = f"Screenshots/{test_name}_{timestamp}.png"
        driver.save_screenshot(filepath)
        return filepath
