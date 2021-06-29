from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="name_edited", header="header_edited", footer="footer_edited"))


def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="name_edited"))


def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="Header modified"))


def test_modify_first_group_footer(app):
    app.group.modify_first_group(Group(footer="Footer modified"))
