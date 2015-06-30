import os
from whatsapp_secretary.utils import get_rules, accepted
from whatsapp_secretary.config import load

CONFIG_FILE = os.path.abspath('test/fixtures/config.json')

def test_get_rules():

    config = load(CONFIG_FILE)

    rules = get_rules("NUMBER1", config)

    assert rules == {'only': 'only'}

def test_accepted():

    assert True == accepted({'only': 'only'}, "This is just a text message which contains only")
    assert False == accepted({'only': 'only'}, "This is just a text message which contains ...")

