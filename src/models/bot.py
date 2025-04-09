from typing import NamedTuple
from selenium.webdriver import Chrome
import chromedriver_autoinstaller
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.models.quote import Quote
from loguru import logger
from selenium.webdriver.chrome.options import Options


class QuotesBot:

    def __init__(self, pages: int, headless: bool = False):

        self._pages = pages
        self._headless = headless
        self._quotes: list[Quote] = []
        self._setup()

        self._url = "https://quotes.toscrape.com"

    def _setup(self):
        chromedriver_autoinstaller.install()

        # modo headless
        options = Options()

        if self._headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        self._driver = Chrome(options=options)

    def _scrap_page(self):
        quote_list = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_any_elements_located((By.CLASS_NAME, "quote"))
        )

        for quote in quote_list:
            text = quote.find_element(By.CSS_SELECTOR, ".text")
            autor = quote.find_element(By.CSS_SELECTOR, ".author")
            tags = quote.find_elements(By.CSS_SELECTOR, ".tag")

            quote = Quote(text.text[1:-1], autor.text)
            quote.tags = [tag.text for tag in tags]

            self._quotes.append(quote)

        self._driver.find_element(By.CSS_SELECTOR, "li.next > a").click()

    def processar(self):
        logger.info("Iniciando raspagem...")
        self._driver.get(self._url)

        for index, _ in enumerate(range(self._pages), start=1):
            logger.info("Raspando página {}", index)
            self._scrap_page()
            logger.info("Total registros raspados: {}.", len(self._quotes))

        self._driver.quit()

    @property
    def quotes(self):
        return self._quotes
