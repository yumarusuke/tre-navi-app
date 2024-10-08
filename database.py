from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    age = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.
db.create_tables([Person])
Person.create(name="ゆうや", age=11)

class Traveler(Model):
    name = CharField()
    age = IntegerField()
    from_area = CharField()
    allergy = CharField()
    dislike = CharField()
    interest = CharField()
    from_date = IntegerField()
    to_date = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.
db.create_tables([Traveler])
