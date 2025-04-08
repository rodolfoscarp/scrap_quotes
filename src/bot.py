from typing import NamedTuple
from selenium.webdriver import Chrome
import chromedriver_autoinstaller
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dataclasses import dataclass, field


@dataclass
class Quote:
    text: str
    autor: str
    tags: list[str] = field(default_factory=list)


class QuotesBot:

    def __init__(self):
        self._quotes: list[Quote] = []
        self._setup()

        self._url = "https://quotes.toscrape.com"

    def _setup(self):
        chromedriver_autoinstaller.install()
        self._driver = Chrome()
        self._driver.maximize_window()

    def _scrap_page(self):
        quote_list = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_any_elements_located((By.CLASS_NAME, "quote"))
        )

        for quote in quote_list:
            text = quote.find_element(By.CSS_SELECTOR, ".text")
            autor = quote.find_element(By.CSS_SELECTOR, ".author")
            tags = quote.find_elements(By.CSS_SELECTOR, ".tag")

            quote = Quote(text.text, autor.text)
            quote.tags = [tag.text for tag in tags]

            self._quotes.append(quote)

        self._driver.find_element(By.CSS_SELECTOR, "li.next > a").click()

    def processar(self):
        self._driver.get(self._url)

        for page in range(3):
            self._scrap_page()

        self._driver.quit()

    @property
    def quotes(self):
        return self._quotes
