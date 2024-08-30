from datetime import datetime

from django.db.models import (
    DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField, DecimalField
)


class Brand(Model):
    name_brand = CharField(max_length=50)
    description_brand = TextField()

    def __str__(self):
        return f"Značka: {self.name_brand} - {self.description_brand}"


class BodyType(Model):
    name_body = CharField(max_length=50)
    description_body = TextField()

    def __str__(self):
        return f"""
        Typ karoserie: {self.name_body}, 
        Popis karoserie: {self.description_body}
        """


class Car(Model):
    name_brand = ForeignKey(Brand, on_delete=DO_NOTHING)
    name_car = CharField(max_length=50, default="")
    name_body = ForeignKey(BodyType, on_delete=DO_NOTHING)
    engine_power = CharField(max_length=20)
    year_of_manufature = CharField(max_length=4)
    date_added = DateTimeField(default=datetime.now)


    def __str__(self):
        return f"{self.name_car} - {self.year_of_manufature}"


class CarOffer(Model):
    name_car = ForeignKey(Car, on_delete=DO_NOTHING)
    offer_description = TextField()
    price = DecimalField(max_digits=11, decimal_places=2)
    date_added = DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.name_car}"

class CommentOffer(Model):
    username = CharField(max_length=64)
    offer = ForeignKey(CarOffer, on_delete=DO_NOTHING)
    text = TextField()
    commented_date = DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.username} - {self.text}"




