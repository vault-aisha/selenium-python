from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_reader import get_config

def get_driver():
    browser = get_config("browser", "name").lower()

    if browser == "chrome":
        options = Options()

        # 1️⃣ Start maximized
        options.add_argument("--start-maximized")

        # 2️⃣ Incognito
        if get_config("browser", "incognito").lower() == "true":
            options.add_argument("--incognito")

        # 3️⃣ Headless
        if get_config("browser", "headless").lower() == "true":
            options.add_argument("--headless=new")  # works better in Chrome 109+

        # 4️⃣ Disable notifications
        if get_config("browser", "disable_notifications").lower() == "true":
            options.add_argument("--disable-notifications")

        # 5️⃣ Window size (headless may need explicit size)
        width = get_config("browser", "window_width")
        height = get_config("browser", "window_height")
        options.add_argument(f"--window-size={width},{height}")

        # 6️⃣ Initialize driver
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # 7️⃣ Implicit wait
    driver.implicitly_wait(5)
    return driver
