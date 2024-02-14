import pytest
from bottle import request

from Assignment1 import todo_list, new_item, edit_item, show_item


# Mock database connection and cursor for testing
class MockCursor:
    def __init__(self, data):
        self.data = data

    def execute(self, query, params=None):
        pass

    def fetchall(self):
        return self.data


class MockConnection:
    def cursor(self):
        return MockCursor([])


# Mock the bottle.request object
class MockRequest:
    GET = {}

    @staticmethod
    def reset():
        MockRequest.GET = {}


@pytest.fixture
def mock_conn(monkeypatch):
    monkeypatch.setattr('Assignment_1.sqlite3.connect', MockConnection)


@pytest.fixture
def mock_request(monkeypatch):
    monkeypatch.setattr('Assignment_1.request', MockRequest)


def test_todo_list(mock_conn):
    result = todo_list()
    assert '<table>' in result
    assert 'todo.db' in result  # Ensure the database name is in the HTML response


def test_new_item(mock_conn, mock_request):
    MockRequest.GET = {'task': 'New Task', 'save': True}
    result = new_item()
    assert 'The new task was inserted into the database' in result


def test_edit_item(mock_conn, mock_request):
    MockRequest.GET = {'task': 'Updated Task', 'status': 'open', 'save': True}
    result = edit_item(1)
    assert 'successfully updated' in result


def test_show_item(mock_conn):
    result = show_item(1)
    assert 'This item number does not exist!' not in result


# Add more test cases as needed for your application
