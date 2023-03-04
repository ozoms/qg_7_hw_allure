import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def form_management_function():

    yield

    browser.quit()
