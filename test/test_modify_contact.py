import datetime
import os
import random
from random import randrange
from model.secondary import Secondary
from model.contact import Contact


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="NameBefore Modify"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_mdf = Contact(firstname="NewModify", middlename="NewMiddleNameModify", lastname="NewEdited",
                               nickname="NewEdited-oss", photo=None, title=None,
                               company="Edited", address="Edited",
                               t_home="888888888", t_mobile="87777777777", t_work="567890987",
                               t_fax="567890987",
                               email="Edited", email2="", email3="", homepage="https://Edited.it",
                               birthdate=datetime.date(1999, 10, 8), anniversary=None,
                               secondary=Secondary("Edited second address", "Edited home phone", "Edited notes"),
                          id=contact.id)
    app.contact.modify_contact_by_id(contact_mdf, contact.id)
    new_contact = db.get_contact_list()
    old_contacts = list(map(lambda x: x if x != contact else contact_mdf, old_contacts))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)


def test_modify_contact_birthdate(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(birthdate=datetime.date(1981, 1, 8)))
    old_contacts = db.get_contact_list()
    contact_old = random.choice(old_contacts)
    contact_mdf = Contact(birthdate=datetime.date(1995, 2, 1))
    contact_mdf.id = contact_old.id
    app.contact.modify_contact_by_id(contact_mdf, contact_old.id)
    new_contacts = db.get_contact_list()
    old_contacts = list(map(lambda x: x if x != contact_old else contact_mdf, old_contacts))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

