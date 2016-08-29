import pytest

from pyramid import testing

ITEMS_TO_CHECK = [
    'title',
    'creation_date',
    'body'
]

@pytest.mark.parametrize('value_to_return', ITEMS_TO_CHECK)
def test_detail_view(value_to_return):
    from .views import detail_view
    request = testing.DummyRequest()
    info = detail_view(request)
    assert value_to_return in info

# ------- Functional Tests -------


@pytest.fixture()
def testapp():
    from myproject import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_layout_root(testapp):
    response = testapp.get('/', status=200)
    assert b'Created in the Code Fellows 401 Python Program' in response.body


def test_root_contents(testapp):
    """Test that the contents of the root page contains as many <article> tags as journal entries."""
    from .views import ENTRIES

    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll("article"))
