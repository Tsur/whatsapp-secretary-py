from utils import get_rules, accepted
from config import load

def test_get_rules():

    config = load("config.json")

    rules = get_rules("NUMBER", config)

    assert rules == {'only': 'only'}

def test_accepted():

    assert True == accepted({'only': 'only'}, "This is just a text message which contains only")
    assert False == accepted({'only': 'only'}, "This is just a text message which contains ...")

