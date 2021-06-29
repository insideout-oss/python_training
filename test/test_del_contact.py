

def test_delete_first_contact(app):
    app.contact.delete_first_contact()


def test_delete_contact_via_edit(app):
    app.contact.delete_first_contact_via_edit()

