import tinydb

db = tinydb.TinyDB('new.db')
# db.insert({'name': 'B', 'surname': 'C'})
person = tinydb.Query()
print(db.search(person.surname == 'C'))
# db.remove(doc_ids=[1])
for person in db:
    # db.update({'age': 18}, doc_ids=[person.doc_id])
    print(person.doc_id, person)
rooms = db.table('rooms')
print(rooms.all())
# rooms.insert({'no': 203})