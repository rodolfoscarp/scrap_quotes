from peewee import Model, ForeignKeyField, CharField, SqliteDatabase, ManyToManyField

db = SqliteDatabase(
    "database.db",
    pragmas={
        "journal_mode": "wal",
        "cache_size": -1 * 64000,  # 64MB
        "foreign_keys": 1,
        "ignore_check_constraints": 0,
        "synchronous": 0,
    },
)


class BaseModel(Model):
    class Meta:
        database = db


class Autor(BaseModel):
    name = CharField(unique=True)


class Quote(BaseModel):
    text = CharField(unique=True)
    autor = ForeignKeyField(Autor, backref="quotes")


class Tag(BaseModel):
    tag = CharField(unique=True)
    quotes = ManyToManyField(Quote, backref="tags")


TagQuote = Tag.quotes.get_through_model()
TagQuote._meta.table_name = "tag_quote"


db.connect()
db.create_tables([Autor, Quote, Tag, TagQuote])
