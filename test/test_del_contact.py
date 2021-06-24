

def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact(10)
    app.session.logout()
