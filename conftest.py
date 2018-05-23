import pytest
import allure
from allure_commons.types import AttachmentType
from fixture.application import Application
import datetime

previous_tests_failed_number = 0


@pytest.fixture(scope="function")
def app(request):
    fixture = Application()
    fixture.set_up()

    request.addfinalizer(fixture.destroy)

    return fixture
