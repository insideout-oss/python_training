import importlib
import json
import os.path
import jsonpickle
import pytest

from fixture.application import Application
from fixture.db import DbFixture
from fixture.orm import ORMFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture
def app(request):
    global fixture
    web_config = load_config(request.config.getoption("--target"))['web']
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])

    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session")
def ormdb(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    ormdbfixture = ORMFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])

    def fin():
        pass
    request.addfinalizer(fin)
    return ormdbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


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

