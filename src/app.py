from src.models.bot import QuotesBot
from dotenv import load_dotenv
import os
from src.services.db_services import DBServices
from src.logs import setup_logs


def start_app():

    setup_logs()
    load_dotenv()

    PAGES = int(os.environ.get("PAGES", 3))

    bot = QuotesBot(PAGES)
    bot.processar()

    for quote in bot.quotes:
        DBServices.save(quote.autor, quote.text, quote.tags)
