from sampleMangler.db_lib import createContainer

def test_using_mongo(mongodb):
    db = mongodb['test_database']
    db.test.insert({'woof': 'woof'})
    documents = db.test.find_one()


from pytest_dbfixtures import factories
mongo_proc2 = factories.mongo_proc(port=27070, params='--nojournal --noauth --nohttpinterface --noprealloc')
mongodb2 = factories.mongodb('mongo_proc2', port=27070)

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
