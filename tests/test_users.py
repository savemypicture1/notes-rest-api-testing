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


def test_forgot_password(registration_login_deleting, email):
    response = registration_login_deleting.post_users_forgot_password(email)

    assert response["success"] is True
    assert response["message"] == f"Password reset link successfully sent to {email}. Please verify by clicking on the given link"


def test_forgot_password_with_unregistered_email(notes_service, email):
    response = notes_service.post_users_forgot_password(email, expected_status_code=401)

    assert response["success"] is False
    assert response["message"] == "No account found with the given email address"


def test_forgot_password_with_invalid_data(notes_service):
    response = notes_service.post_users_forgot_password("invalid@email", expected_status_code=400)

    assert response["success"] is False
    assert response["message"] == "A valid email address is required"


def test_change_password(registration_login_deleting, password, new_password):
    response = registration_login_deleting.post_users_change_password(password, new_password)

    assert response["success"] is True
    assert response["message"] == "The password was successfully updated"


def test_change_password_with_invalid_data(registration_login_deleting, new_password):
    response = registration_login_deleting.post_users_change_password("falsy_password", new_password, expected_status_code=400)

    assert response["success"] is False
    assert response["message"] == "The current password is incorrect"


def test_login_after_change_password(registration_login_deleting, email, password, new_password):
    registration_login_deleting.post_users_change_password(password, new_password)
    response = registration_login_deleting.post_users_login(email, new_password)

    assert response["data"]["token"] is not None


def test_logout(registration_login_login_deleting):
    response = registration_login_login_deleting.delete_users_logout()

    assert response["success"] is True
    assert response["message"] == "User has been successfully logged out"


def test_logout_without_login(notes_service):
    response = notes_service.delete_users_logout(expected_status_code=401)

    assert response["success"] is False
    assert response["message"] == "No authentication token specified in x-auth-token header"


def test_deleting_account(registration, email, password):
    registration.post_users_login(email, password)
    response = registration.delete_user_account()

    assert response["success"] is True
    assert response["message"] == "Account successfully deleted"


def test_deleting_account_without_login(notes_service):
    response = notes_service.delete_user_account(expected_status_code=401)

    assert response["success"] is False
    assert response["message"] == "No authentication token specified in x-auth-token header"
