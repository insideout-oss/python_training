

def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first_group()
    app.session.logout()


def test_delete_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete(10)
    app.session.logout()

