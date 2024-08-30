from django.db.models import (
    DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField, DecimalField,
)


class Brand(Model):
    name_brand = CharField(max_length=50)
    description_brand = TextField()

    def __str__(self):
        return f"Značka automobilu: {self.name_brand}\nPředstavení značky: {self.description_brand}"


class BodyType(Model):
    name_body = CharField(max_length=50)


class Car(Model):
    name_brand = ForeignKey(Brand, on_delete=DO_NOTHING)
    name_body = ForeignKey(BodyType, on_delete=DO_NOTHING)
    description_car = (TextField)
    engine_power = CharField(max_length=20)
    year_of_manufature = IntegerField(max_length=4)
    price = DecimalField(max_digits=11, decimal_places=2)
    date_added = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""
        Značka automobilu: {self.name_brand}
        Typ karoserie: {self.name_body}
        Výkon: {self.engine_power}
        Rok výroby: {self.year_of_manufature}
        Cena: {self.price}
        """



