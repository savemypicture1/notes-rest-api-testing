import os
from logging import getLogger
import pytest
from rest.notes_rest import NotesRest


logger = getLogger(__name__)


@pytest.fixture(scope="session")
def name():
    return os.getenv("NAME")


@pytest.fixture(scope="session")
def email():
    return os.getenv("EMAIL")


@pytest.fixture(scope="session")
def password():
    return os.getenv("PASSWORD")


@pytest.fixture(scope="session")
def new_password():
    return os.getenv("NEW_PASSWORD")


@pytest.fixture
def notes_service():
    return NotesRest()


@pytest.fixture
def authenticated_notes_service(registration, email, password):
    registration.post_users_login(email, password)
    yield registration
    registration.delete_user_account()


@pytest.fixture
def prepared_note(authenticated_notes_service) -> dict:
    logger.info("Preparing note for tests")
    response = authenticated_notes_service.post_notes(
        title="Test Title",
        description="Test Description",
        category="Home",
        expected_status_code=200
    )
    logger.info(f"Note prepared: {response['data']}")

    return response["data"], authenticated_notes_service


@pytest.fixture
def registration(notes_service, name, email, password):
    logger.info("Registration account")
    notes_service.post_users_register(name, email, password)

    return notes_service


@pytest.fixture
def log_in_with_deleting_account_for_registration(notes_service, email, password):
    yield notes_service
    logger.info("Log in")
    notes_service.post_users_login(email, password)
    logger.info("Deleting account")
    delete = notes_service.delete_user_account()
    logger.info(delete["message"])


@pytest.fixture
def registration_with_deleting_account(registration):
    yield registration
    logger.info("Deleting account")
    delete = registration.delete_user_account()
    logger.info(delete["message"])


@pytest.fixture
def registration_login_deleting(registration, email, password):
    logger.info("Log in")
    registration.post_users_login(email, password)
    yield registration
    logger.info("Deleting account")
    delete = registration.delete_user_account()
    logger.info(delete["message"])


@pytest.fixture
def registration_login_login_deleting(registration_login_deleting, email, password):
    yield registration_login_deleting
    logger.info("Log in")
    registration_login_deleting.post_users_login(email, password)
