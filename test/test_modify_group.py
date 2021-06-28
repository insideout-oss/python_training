from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="name_edited", header="header_edited", footer="footer_edited"))
    app.session.logout()


def test_modify_first_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="name_edited", header=None, footer=None))
    app.session.logout()


def test_modify_first_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name=None, header="Header modified", footer=None))
    app.session.logout()


def test_modify_first_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name=None, header=None, footer="Footer modified"))
    app.session.logout()
