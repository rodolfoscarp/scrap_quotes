from src.models.bot import QuotesBot
from dotenv import load_dotenv
import os
from src.services import DBServices, APIServices
from src.logs import setup_logs
from loguru import logger


def start_app():

    setup_logs()
    load_dotenv()

    PAGES = int(os.environ.get("PAGES", 3))
    APIURL = os.environ.get("APIURL")
    HEADLESS = bool(int(os.environ.get("HEADLESS", 1)))

    bot = QuotesBot(PAGES, HEADLESS)
    bot.processar()

    logger.info("Salvando registros no banco e API.")

    for quote in bot.quotes:
        logger.debug("Salvando regitros: {} - {}", quote.autor, quote.text)
        DBServices.save(quote.autor, quote.text, quote.tags)
        APIServices.create(APIURL, quote.autor, quote.text, quote.tags)
