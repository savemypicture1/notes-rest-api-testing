# import pytest
#
#
# @pytest.mark.parametrize("category", ["Home", "Work", "Personal"])
# def test_create_note(authenticated_notes_service, category):
#     title = "Test note"
#     description = "Test Description"
#
#     response = authenticated_notes_service.post_notes(title, description, category)
#
#     assert response["message"] == "Note successfully created"
#     assert response["data"]["title"] == title
#     assert response["data"]["description"] == description
#     assert response["data"]["category"] == category
#     assert response["data"]["id"] is not None
#
#
# def test_create_note_invalid_category(authenticated_notes_service):
#     title = "Test note"
#     description = "Test Description"
#     category = "Invalid"
#
#     response = authenticated_notes_service.post_notes(title, description, category, expected_status_code=400)
#
#     assert response["message"] == "Category must be one of the categories: Home, Work, Personal"
#
#
# def test_delete_note_by_id(authenticated_notes_service, prepared_note):
#     response = authenticated_notes_service.delete_note_by_id(prepared_note["id"])
#
#     assert response["message"] == "Note successfully deleted"
