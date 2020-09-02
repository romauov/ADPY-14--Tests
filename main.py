from data.directories import directories
from data.documents import documents
from funcs import *
import pytest
from pytest_mock import mock
import builtins
import json



class TestDataOrganizer:

    def setup(self):
        print("method setup")

    def teardown(self):
        print("method teardown")

    def test_shelf_search(self):
        with open('fixtures/directories.json', 'r', encoding='utf-8') as f:
            test_dir = json.load(f)
        with mock.patch.object(builtins, 'input', lambda _: '11-2'):
            assert shelf_search() == list(test_dir.keys())[0]

    def test_people_search(self):
        with open('fixtures/documents.json', 'r', encoding='utf-8') as f:
            test_doc = json.load(f)
        with mock.patch.object(builtins, 'input', lambda _: '10006'):
            assert people_search() == test_doc[2]['name']

    def test_add_new_doc(self):
        assert add_new_doc('doc_type', 'some_id', 'just_another_name', '1') == 'документ doc_type some_id just_another_name был добавлен на  полку 1'

    def test_doc_delete(self):
        assert doc_delete('11-2') == 'Документ 11-2 удалён'




if __name__ == '__main__':
    print(add_new_doc('doc_type', 'some_id', 'just_another_name', '1'))

    # data_organizer()