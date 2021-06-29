from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="", header="", footer=""))
    app.group.modify_first_group(Group(name="name_edited", header="header_edited", footer="footer_edited"))


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Needs to be modified"))
    app.group.modify_first_group(Group(name="name_edited"))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="Needs to be modified"))
    app.group.modify_first_group(Group(header="Header modified"))


def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="Needs to be modified"))
    app.group.modify_first_group(Group(footer="Footer modified"))
