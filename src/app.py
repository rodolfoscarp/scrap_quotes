from src.models.bot import QuotesBot
from dotenv import load_dotenv
import os
from src.services.db_services import DBServices


load_dotenv()


def start_app():

    PAGES = int(os.environ.get("PAGES", 3))

    bot = QuotesBot(PAGES)
    bot.processar()

    for quote in bot.quotes:
        DBServices.save(quote.autor, quote.text, quote.tags)
