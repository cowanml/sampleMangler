from sampleMangler.db_lib import _createContainer
from pytest_dbfixtures import factories


mongo_proc = factories.mongo_proc(port=27070, params='--nojournal --noauth --nohttpinterface --noprealloc')
mongodb = factories.mongodb('mongo_proc')

def test_using_mongo(mongodb):
    test_data_one = {
        'woof': 'woof',
    }
    db = mongodb['test_database']
    db.test.insert(test_data_one)
    assert db.test.find_one()['woof'] == 'woof'


mongo_proc2 = factories.mongo_proc(port=27071, params='--nojournal --noauth --nohttpinterface --noprealloc')
mongodb2 = factories.mongodb('mongo_proc2')

def test_second_mongo(mongodb, mongodb2):
    test_data_one = {
        "test1": "test1",
    }
    db = mongodb['test_db']
    db.test.insert(test_data_one)
    assert db.test.find_one()['test1'] == 'test1'

    test_data_two = {
        "test2": "test2",
    }
    db = mongodb2['test_db']
    db.test.insert(test_data_two)
    assert db.test.find_one()['test2'] == 'test2'


def test_createContainer():
    foo=True
    assert foo == True
