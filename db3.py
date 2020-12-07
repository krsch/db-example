import ZODB, ZODB.FileStorage
import BTrees.OOBTree
import persistent
from dataclasses import dataclass, field
import datetime

connection = ZODB.connection('mydata.fs')
root = connection.root

@dataclass
class Person(persistent.Persistent):
    name: str
    birthday: datetime.date
    friends: list = field(default_factory=list)

# root.people = [Person('A', datetime.date(2000,1,1))]
def create_people():
    print(root)
    root.people = BTrees.OOBTree.BTree()
    root.people['A'] = Person('A', datetime.date(2000,1,1))


print(root, root.people)
print(root.people['A'])
# for key, person in root.people.items():
#     print(key,person)
# root.people['A'].name = 'AAA'

# import transaction
# transaction.commit()