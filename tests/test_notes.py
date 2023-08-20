import pytest

@pytest.mark.parametrize("category", ["Home", "Work", "Personal"])
def test_create_note(authenticated_notes_service, category):
    title = "Test note"
    description = "Test Description"

    response = authenticated_notes_service.post_notes(title, description, category)

    assert response["message"] == "Note successfully created"
    assert response["data"]["title"] == title
    assert response["data"]["description"] == description
    assert response["data"]["category"] == category
    assert response["data"]["id"] is not None


def test_create_note_invalid_category(authenticated_notes_service):
    title = "Test note"
    description = "Test Description"
    category = "Invalid"

    response = authenticated_notes_service.post_notes(title, description, category, expected_status_code=400)

    assert response["message"] == "Category must be one of the categories: Home, Work, Personal"


def test_getting_notes(prepared_note):
    data, note_service = prepared_note
    response = note_service.get_notes()

    assert response["data"][0]["title"] == data["title"]
    assert response["data"][0]["description"] == data["description"]
    assert response["data"][0]["category"] == data["category"]
    assert response["data"][0]["id"] is not None


def test_getting_notes_without_login(notes_service):
    response = notes_service.get_notes(expected_status_code=401)

    assert response["success"] is False
    assert response["message"] == "No authentication token specified in x-auth-token header"


def test_getting_notes_by_id(prepared_note):
    data, note_service = prepared_note
    response = note_service.get_notes_by_id(data["id"])

    assert response["data"]["title"] == data["title"]
    assert response["data"]["description"] == data["description"]
    assert response["data"]["category"] == data["category"]
    assert response["data"]["id"] == data["id"]


def test_getting_notes_by_id_with_incorrect_id(authenticated_notes_service):
    response = authenticated_notes_service.get_notes_by_id("id", expected_status_code=400)

    assert response["success"] is False
    assert response["message"] == "Note ID must be a valid ID"


def test_getting_notes_by_id_without_login(notes_service):
    response = notes_service.get_notes_by_id("id", expected_status_code=401)

    assert response["success"] is False
    assert response["message"] == "No authentication token specified in x-auth-token header"


def test_update_note(prepared_note):
    data, note_service = prepared_note
    response = note_service.put_note_by_id(data["id"], "title", "description", "Work")

    assert response["data"]["title"] == "title"
    assert response["data"]["description"] == "description"
    assert response["data"]["category"] == "Work"
    assert response["success"] is True
    assert response["message"] == "Note successfully Updated"


def test_update_note_with_invalid_data(prepared_note):
    data, note_service = prepared_note
    response = note_service.put_note_by_id(data["id"], "", "", "Work", expected_status_code=400)

    assert response["success"] is False


def test_update_note_without_login(notes_service):
    response = notes_service.put_note_by_id("id", "title", "description", "Work", expected_status_code=401)

    assert response["success"] is False
    assert response["message"] == "No authentication token specified in x-auth-token header"


def test_update_status_note(prepared_note):
    data, note_service = prepared_note
    response = note_service.patch_notes_by_id(data["id"], True)

    assert response["data"]["completed"] is True
    assert response["success"] is True
    assert response["message"] == "Note successfully Updated"


def test_update_status_note_with_invalid_data(prepared_note):
    data, note_service = prepared_note
    response = note_service.patch_notes_by_id(data["id"], "True", expected_status_code=400)

    assert response["success"] is False


def test_update_status_note_without_login(notes_service):
    response = notes_service.patch_notes_by_id("id", True, expected_status_code=401)

    assert response["success"] is False
    assert response["message"] == "No authentication token specified in x-auth-token header"


def test_delete_note_by_id(prepared_note):
    data, note_service = prepared_note
    response = note_service.delete_note_by_id(data["id"])

    assert response["success"] is True
    assert response["message"] == "Note successfully deleted"


def test_delete_note_by_id_with_incorrect_id(authenticated_notes_service):
    response = authenticated_notes_service.delete_note_by_id("id", expected_status_code=400)

    assert response["success"] is False
    assert response["message"] == "Note ID must be a valid ID"


def test_delete_note_by_id_without_login(notes_service):
    response = notes_service.delete_note_by_id("id", expected_status_code=401)

    assert response["success"] is False
    assert response["message"] == "No authentication token specified in x-auth-token header"
