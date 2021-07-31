from fixture.db import DbFixture
from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    ll = db.get_contacts_not_in_group(Group(id='102'))
    for item in ll:
        print(item)
    print(len(ll))
finally:
    pass

