from django.db.models import (
    DO_NOTHING, CharField, DateField, DateTimeField, ForeignKey, IntegerField,
    Model, TextField
)

class Brand(Model):
    name_brand = CharField(max_length=50)
    description = TextField()

    def __str__(self):
        return f"Značka automobilu: {self.name_brand}\nPředstavení značky: {self.description}"
