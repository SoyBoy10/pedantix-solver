from selenium import webdriver
import sys

from selenium.webdriver.chrome.webdriver import WebDriver


class BrowserHelper:

    def __init__(self, browser: str, no_ui: bool, website_address: str = "cemantix.certitudes.org/pedantix"):
        self.browser = browser
        self.no_ui = no_ui
        self.website_address = website_address
        self.driver = self._setup_driver()

    def _setup_driver(self) -> WebDriver:
        if self.browser == "firefox":
            if self.no_ui:
                opt = webdriver.FirefoxOptions()
                opt.add_argument('-headless')
                driver = webdriver.Firefox(options=opt)
            else:
                driver = webdriver.Firefox()
        elif self.browser == "edge":
            if self.no_ui:
                opt = webdriver.EdgeOptions()
                opt.add_argument('--headless')
                driver = webdriver.Edge(options=opt)
            else:
                driver = webdriver.Edge()
        elif self.browser == "safari":
            if self.no_ui:
                print("ERROR : Safari can't be run without UI, sorry :(")
                sys.exit(0)
            else:
                driver = webdriver.Safari()
        elif self.browser == "chrome":
            if self.no_ui:
                opt = webdriver.ChromeOptions()
                opt.add_argument('--headless')
                driver = webdriver.Chrome(options=opt)
            else:
                driver = webdriver.Chrome()
        else:
            print("Error : unrecognized browser...")
            sys.exit(0)
        driver.get('https://' + self.website_address)
        driver.find_element('id', 'dialog-close').click()
        return driver

    def input_guess(self, input_value: str) -> dict:
        self.driver.find_element("id", "pedantix-guess").send_keys(input_value)
        self.driver.find_element("id", "pedantix-guess-btn").click()
        text_res = self.driver.find_element("id", "pedantix-error").text
        return {
            "🟥": text_res.count("🟥"),
            "🟧": text_res.count("🟧"),
            "🟩": text_res.count("🟩"),
        }

    def get_article(self) -> list[str]:
        article = self.driver.find_element("id", "article")
        return article.text.split("\n")
