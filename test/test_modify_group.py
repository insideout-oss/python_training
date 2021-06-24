from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="name_edited", header="header_edited", footer="footer_edited"),
                     index=1)
    app.session.logout()


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_name(name="name_edited", index=1)
    app.session.logout()


def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_header(header="header_edited", index=1)
    app.session.logout()


def test_modify_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_footer(footer="footer_edited", index=1)
    app.session.logout()
