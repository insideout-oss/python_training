# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test_group", header="test_group_header", footer="test_group_footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
