import importlib
import json
import os.path

import jsonpickle
import pytest

from fixture.application import Application

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target"))
        with open(config_file) as f:
            target = json.load(f)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target['baseUrl'])

    fixture.session.ensure_login(target['username'], target['password'])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")


def pytest_generate_tests(metafunc):
    for f in metafunc.fixturenames:
        if f.startswith("data_"):
            testdata = load_from_module(f[5:])
            metafunc.parametrize(f, testdata, ids=[str(x) for x in testdata])
        elif f.startswith("json_"):
            testdata = load_from_json(f[5:])
            metafunc.parametrize(f, testdata, ids=[str(x) for x in testdata])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)
    with open(fn) as f:
        return jsonpickle.decode(f.read())

