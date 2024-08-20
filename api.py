import httpx
import json


class scim_api():
    def __init__(self, base_url, token):
        """
        Initializes a new instance of the class with the given base URL and token.

        Parameters:
            base_url (str): The base URL for the API.
            token (str): The authentication token.

        Returns:
            None
        """
        self.base_url = base_url
        self.token = token
        self.headers = {'Authorization': f'Bearer {token}',
                        'Content-Type': 'application/json'}
        self.client = httpx.Client(headers=self.headers)

    def call_api(self, path, method, payload=None):
        """
        Makes an HTTP request to the specified path using the given method and payload.

        Parameters:
            path (str): The path of the API endpoint to call.
            method (str): The HTTP method to use (e.g. 'GET', 'POST', 'DELETE', etc.).
            payload (dict, optional): The JSON payload to send with the request. Defaults to None.

        Returns:
            dict or int: The JSON response from the server, or the status code if the method is 'DELETE'.
        """
        if method not in ('GET', 'POST', 'DELETE', 'PUT', 'PATCH'):
            print(f'Invalid Method {method}')
            return
        try:
            response = self.client.request(method, path, json=payload)
            response.raise_for_status()
            if method in ('GET', 'POST', 'PUT', 'PATCH'):
                result = json.loads(response.text)
            else:
                result = {'Success': f'{response.status_code}'}
        except Exception as e:
            print(e)
            result = {'Error': f'{str(e)}'}
        finally:
            return result

    def get_all_users(self):
        """
        Retrieves all users from the API.

        Returns:
            The response from the API call.
        """
        path = f'{self.base_url}/Users'
        return self.call_api(path, 'GET')

    def get_user(self, user_id):
        """
        Retrieves a user from the API based on the provided user ID.

        Parameters:
            user_id (str): The ID of the user to retrieve.

        Returns:
            dict: A dictionary representing the user data.

        Raises:
            requests.exceptions.RequestException: If there is an error making the API request.
        """
        path = f'{self.base_url}/Users/{user_id}'
        return self.call_api(path, 'GET')

    def create_user(self, **kwargs):
        """
        Creates a new user in the SCIM API.

        Parameters:
            external_id (str, optional): The external ID of the user.
            username (str, optional): The username of the user.
            given_name (str, optional): The given name of the user.
            family_name (str, optional): The family name of the user.
            email (str, optional): The email address of the user.
            payload (dict, optional): A custom payload to send with the request.

        Returns:
            dict: The JSON response from the server.
        """
        path = f'{self.base_url}/Users'
        external_id = kwargs.get('external_id', None)
        username = kwargs.get('username', None)
        given_name = kwargs.get('given_name', None)
        family_name = kwargs.get('family_name', None)
        email = kwargs.get('email', None)
        payload = kwargs.get('payload', {
            'schemas': [
                'urn:ietf:params:scim:schemas:core:2.0:User',
                'urn:ietf:params:scim:schemas:extension:enterprise:2.0:User'
            ],
            'externalId': external_id,
            'active': True,
            'userName': username,
            'organization': 'test',
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                "department": "Cloud and Reliability"
            },
            'displayName': f'{given_name} {family_name}',
            'name': {
                'givenName': given_name,
                'familyName': family_name
            },
            "emails": [
                {
                    "value": email
                }]
        })
        return self.call_api(path, 'POST', payload)

    def delete_user(self, user_id):
        """
        Deletes a user from the API based on the provided user ID.

        Parameters:
            user_id (str): The ID of the user to delete.

        Returns:
            int: The status code of the deletion operation.
        """
        path = f'{self.base_url}/Users/{user_id}'
        return self.call_api(path, 'DELETE')

    def get_all_groups(self):
        """
        Retrieves all groups from the API.

        Returns:
            dict: The JSON response from the server containing all groups.
        """
        path = f'{self.base_url}/Groups'
        return self.call_api(path, 'GET')

    def get_group(self, group_id):
        """
        Retrieves a group from the API based on the provided group ID.

        Parameters:
            group_id (str): The ID of the group to retrieve.

        Returns:
            dict: The JSON response from the server containing the group data.
        """
        path = f'{self.base_url}/Groups/{group_id}'
        return self.call_api(path, 'GET')

    def create_group(self, **kwargs):
        """
        Creates a new group in the SCIM API.

        Parameters:
            external_id (str, optional): The external ID of the group.
            name (str, optional): The name of the group.
            members (list, optional): A list of member user IDs.
            payload (dict, optional): A custom payload to send with the request.

        Returns:
            dict: The JSON response from the server.
        """
        path = f'{self.base_url}/Groups'
        external_id = kwargs.get('external_id', None)
        name = kwargs.get('name', None)
        members = kwargs.get('members', None)
        member_list = []
        for member in members:
            member_list.append({'value': member})
        payload = kwargs.get('payload', {
            "schemas": ["urn:ietf:params:scim:schemas:core:2.0:Group"],
            "displayName": name,
            "externalId": external_id,
            "members": member_list})
        return self.call_api(path, 'POST', payload)

    def delete_group(self, group_id):
        """
        Deletes a group from the API based on the provided group ID.

        Parameters:
            group_id (str): The ID of the group to delete.

        Returns:
            int: The status code of the deletion operation.
        """
        path = f'{self.base_url}/Groups/{group_id}'
        return self.call_api(path, 'DELETE')
