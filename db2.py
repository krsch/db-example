import peewee

db = peewee.SqliteDatabase('people.db')

class Person(peewee.Model):
    name = peewee.CharField()  # name : str
    birthday = peewee.DateField()  # birthday : date
    # pets : List[Pet]

    class Meta:
        database = db # This model uses the "people.db" database.


class Pet(peewee.Model):
    owner = peewee.ForeignKeyField(Person, backref='pets')
    name = peewee.CharField()  # name : str
    animal_type = peewee.CharField()  # animal_type : str

    class Meta:
        database = db  # this model uses the "people.db" database


db.connect()
db.create_tables([Person, Pet])

from datetime import date
def create_people():
    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
    uncle_bob.save()  # bob is now stored in the database
    Person.create(name='Grandma', birthday=date(1935, 3, 1))
    Person.create(name='Herb', birthday=date(1950, 5, 5))
grandma = Person.get(Person.name == 'Grandma')
uncle_bob = Person.get(Person.name == 'Bob')
herb = Person.get(Person.name == 'Herb')

def create_pets():
    bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
    herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
    herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

for person in Person:
    if len(person.pets) > 0:
        print(f'{person.name} has pets ' + ", ".join(
            pet.animal_type + " " + pet.name for pet in person.pets
        ))
    else:
        print(f'{person.name} has no pets')

herb_mittens_jr = Pet.get(Pet.name == 'Mittens Jr')
herb_mittens_jr.animal_type = 'kitten'
herb_mittens_jr.save()