# def test_kurwa(log_in_with_deleting_account_for_registration):
#     print('kurwa')

def test_registration(log_in_with_deleting_account_for_registration, name, email, password):
    response = log_in_with_deleting_account_for_registration.post_users_register(name, email, password)

    assert response["success"] is True


def test_registration_with_invalid_credentials(notes_service, name, password):
    response = notes_service.post_users_register(name, "invalidemail.com", password, expected_status_code=400)

    assert response["success"] is False


def test_login(registration_with_deleting_account, email, password):
    response = registration_with_deleting_account.post_users_login(email, password)

    assert response["data"]["token"] is not None


def test_login_with_invalid_credentials(notes_service, password):
    response = notes_service.post_users_login("invalid@email", password, expected_status_code=400)

    assert response["success"] is False


def test_login_with_unregistered_user(notes_service, password):
    response = notes_service.post_users_login("invalid@email.com", password, expected_status_code=401)

    assert response["message"] == "Incorrect email address or password"


def test_profile(registration_login_deleting, email):
    response = registration_login_deleting.get_users_profile()

    assert response["message"] == "Profile successful"
    assert response["data"]["email"] == email, "Email address is not correct"


def test_profile_unauthenticated(notes_service):
    response = notes_service.get_users_profile(expected_status_code=401)

    assert response["success"] is False
    assert response["message"] == "No authentication token specified in x-auth-token header"


def test_update_profile(registration_login_deleting, name):
    response = registration_login_deleting.patch_users_profile(name, "123456789", "Test")

    assert response["success"] is True
    assert response["message"] == "Profile updated successful"


def test_update_profile_with_invalid_data(registration_login_deleting, name):
    response = registration_login_deleting.patch_users_profile(name, "twozerotwofour", "qwerty",expected_status_code=400)

    assert response["success"] is False

def test_update_profile_unauthenticated(notes_service):
    response = notes_service.patch_users_profile(expected_status_code=401)

    assert response["success"] is False
    assert response["message"] == "No authentication token specified in x-auth-token header"
