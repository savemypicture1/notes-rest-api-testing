from rest.rest_client import RestClient


class NotesRest(RestClient):
    """
    Notes API service
    """
    BASE_URL = "https://practice.expandtesting.com/notes/api/"
    _token: str | None = None

    @property
    def _headers(self):
        return {"x-auth-token": self._token}


    def get_health_check(self):
        """
        Send a GET request to /health-check
        :return: response in JSON format
        """
        self._log.info("Checking health")
        response = self._get("health-check")

        return response


    def post_users_register(self, name=None, email=None, password=None, expected_status_code=201):
        """
        Send a POST request to /users/register
        :param name: name
        :param email: email
        :param password: password
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Register with {name} and {email}")
        response = self._post("users/register",
                              json={"name": name, "email": email, "password": password},
                              expected_status_code=expected_status_code)

        return response


    def post_users_login(self, email=None, password=None, expected_status_code=200):
        """
        Send a POST request to /users/login
        :param email: email
        :param password: password
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Logging in as {email}")
        response = self._post("users/login",
                              json={"email": email, "password": password},
                              expected_status_code=expected_status_code)
        if response["status"] == 200:
            self._token = response["data"]["token"]

        return response


    def get_users_profile(self, expected_status_code=200):
        """
        Send a GET request to /users/profile
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("Getting user profile")
        response = self._get("users/profile", expected_status_code=expected_status_code)

        return response


    def patch_users_profile(self, name=None, phone=None, company=None, expected_status_code=200):
        """
        Send a PATCH request to /users/profile
        :param name: name
        :param phone: phone
        :param company: company
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("Update user info")
        response = self._patch("users/profile",
                               json={"name": name, "phone": phone, "company": company},
                               expected_status_code=expected_status_code)

        return response


    def post_users_forgot_password(self, email=None, expected_status_code=200):
        """
        Send a POST request to /users/forgot-password
        :param email: email
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Forgot password for {email}")
        response = self._post("users/forgot-password",
                              json={"email": email},
                              expected_status_code=expected_status_code)

        return response


    def post_users_verify_reset_password_token(self):
        pass


    def post_users_reset_password(self):
        pass


    def post_users_change_password(self, current_password=None, new_password=None, expected_status_code=200):
        """
        Send a POST request to /users/change-password
        :param current_password: current_password
        :param new_password: new_password
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Changing password")
        response = self._post("users/change-password",
                              json={"currentPassword": current_password, "newPassword": new_password},
                              expected_status_code=expected_status_code)

        return response


    def delete_users_logout(self, expected_status_code=200):
        """
        Send a DELETE request to /users/logout
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("Logging out")
        response = self._delete("users/logout", expected_status_code=expected_status_code)
        if response["status"] == 200:
            self._token = None

        return response


    def delete_user_account(self, expected_status_code=200):
        """
        Send a DELETE request to /users/delete-account
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("Deleting account")
        response = self._delete(f"users/delete-account", expected_status_code=expected_status_code)

        return response


    def post_notes(self, title=None, description=None, category=None, expected_status_code=200):
        """
        Send a POST request to /notes
        :param title: title of the note
        :param description: description of the note
        :param category: category of the note (Home, Work, Personal)
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Creating note with title: {title}")
        response = self._post("notes",
                              data={"title": title, "description": description, "category": category},
                              expected_status_code=expected_status_code)

        return response


    def get_notes(self, expected_status_code=200):
        """
        Send a GET request to /notes
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info("Getting notes")
        response = self._get("notes", expected_status_code=expected_status_code)

        return response


    def get_notes_by_id(self, id=None, expected_status_code=200):
        """
        Send a GET request to /notes/id
        :param id: id
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Getting notes by: {id}")
        response = self._get(f"notes/{id}", expected_status_code=expected_status_code)

        return response


    def put_note_by_id(self, id=None, title=None, description=None, category=None, completed=False, expected_status_code=200):
        """
        Send a PUT request to /notes/id
        :param id: id
        :param title: title of the note
        :param description: description of the note
        :param category: category of the note (Home, Work, Personal)
        :param completed: status
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Put note by: {id}")
        response = self._put(f"notes/{id}",
                              json={"title": title, "description": description, "category": category, "completed": completed},
                              expected_status_code=expected_status_code)

        return response


    def patch_notes_by_id(self, id=None, completed=False, expected_status_code=200):
        """
        Send a PATCH request to /notes/id
        :param id: id
        :param completed: status
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Patch note by: {id}")
        response = self._patch(f"notes/{id}",
                              json={"completed": completed},
                              expected_status_code=expected_status_code)

        return response


    def delete_note_by_id(self, note_id=None, expected_status_code=200):
        """
        Send a DELETE request to /notes/{note_id}
        :param note_id: id of the note
        :param expected_status_code: expected status code
        :return: response in JSON format
        """
        self._log.info(f"Deleting note with id: {note_id}")
        response = self._delete(f"notes/{note_id}", expected_status_code=expected_status_code)

        return response
