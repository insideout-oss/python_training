import datetime
from model.contact import Contact
import time


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name1", middlename="MiddleName", lastname="LastName",
                                   nickname="insideout-oss"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    # Without a delay test starts getting contact list before the page is updated
    time.sleep(5)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_contact_via_edit(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="NameBefore Deleted"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact_via_edit()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts

