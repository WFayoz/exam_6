from django.db.models import Model, CharField, URLField, DecimalField, TextChoices, TextField


class Book(Model):
    name = CharField(max_length=255)
    author = CharField(max_length=20)
    price = DecimalField(max_digits=10, decimal_places=0)
    icon = URLField()


class Comment(Model):
    class RatingChoices(TextChoices):
        YAXSHI = 'yaxshi', 'Yaxshi'
        ALO = 'alo', 'Alo'
        QONIQARLI = 'qoniqarli', 'Qoniqarli'

    book_name = CharField(max_length=255)
    rating = CharField(choices=RatingChoices, default=RatingChoices.YAXSHI)
    comment = TextField()
    name = CharField(max_length=255)
