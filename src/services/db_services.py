from peewee import IntegrityError
from src.db import db, Autor, Tag, Quote
from loguru import logger


class DBServices:

    @staticmethod
    def save(autor: str, text: str, tags: list[str]):
        try:
            with db.atomic():
                autor_instance, _ = Autor.get_or_create(name=autor)
                quote_instance, _ = Quote.get_or_create(
                    text=text, autor=autor_instance.id
                )

                for tag in tags:
                    tag, new = Tag.get_or_create(tag=tag)
                    if new:
                        quote_instance.tags.add(tag)

            logger.debug("Registro salvo/atualizado com sucesso.")
        except Exception as e:
            logger.exception(e)
