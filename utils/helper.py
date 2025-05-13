# utils/helper.py

import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{name}_{timestamp}.png"
    screenshot_dir = os.path.join(os.getcwd(), "screenshots")

    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)

    path = os.path.join(screenshot_dir, filename)
    driver.save_screenshot(path)
    return path
