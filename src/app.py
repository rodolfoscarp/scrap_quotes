from src.bot import QuotesBot
from dotenv import load_dotenv
import os
from src.db import Quote, Autor, Tag, db
from peewee import IntegrityError

load_dotenv()


def start_app():

    PAGES = int(os.environ.get("PAGES", 3))

    bot = QuotesBot(PAGES)
    bot.processar()

    for quote in bot.quotes:
        try:
            with db.atomic():
                autor, _ = Autor.get_or_create(name=quote.autor)
                quote_db, _ = Quote.get_or_create(text=quote.text, autor=autor.id)

                for tag in quote.tags:
                    tag, new = Tag.get_or_create(tag=tag)
                    if new:
                        quote_db.tags.add(tag)

        except IntegrityError as e:
            print(f"Erro de integridade: {e}")
