import datetime
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Name1", middlename="MiddleName", lastname="LastName",
                                   nickname="insideout-oss"))
    app.contact.delete_first_contact()


def test_delete_contact_via_edit(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="NameBefore Deleted"))
    app.contact.delete_first_contact_via_edit()

