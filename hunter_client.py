"""
Module for interacting with the Hunter.io API.

This module provides a Python wrapper for the Hunter.io API, allowing users
to perform various tasks such as email verification, domain search,
email finding, and more. It includes an asynchronous client (``HunterAPI``)
with methods corresponding to different API endpoints.
Usage:
1. Initialize ``HunterAPI`` with an API key.
2. Use methods like ``verification_email``, ``search_domain``,
``email_finder``,
etc., to interact with the Hunter.io API.
``
"""

import asyncio
from typing import Any, Dict, Optional

import httpx


class CRUDMixin:

    """
    Mixin class providing basic CRUD (Create, Read, Update, Delete),
    operations.

    This class includes methods for creating, reading, updating,
    and deleting results stored in a dictionary. It serves as a base class
    to be inherited by other classes requiring CRUD functionality.

    Methods:
    - create_result(key: str, result: Dict[str, Any]) -> None:
    Create a new result.
    - read_result(key: str) -> Optional[Dict[str, Any]]:
    Get the result by key.
    - update_result(key: str, new_result: Dict[str, Any]) -> None:
    Refresh result by key.
    - delete_result(key: str) -> None:
    Delete the result by key.

    Attributes:
    - _results (Dict[str, Any]): A dictionary to store results.
    """

    def __init__(self):
        """
        Initialize the CRUDMixin object.

        This method creates an empty dictionary (_results) to store results.
        """
        self._results = {}

    def create_result(self, key: str, result: Dict[str, Any]) -> None:
        """
        Create a new result and store it with the provided key.

        Args:
            key (str): The key for the new result.
            result (Dict[str, Any]): The result to be stored.
        """
        self._results[key] = result

    def read_result(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Get the result by key.

        Args:
            key (str): The key to look up.

        Returns:
            Optional[Dict[str, Any]]: The result corresponding to the key,
            or None if the key is not found.
        """
        return self._results.get(key)

    def update_result(self, key: str, new_result: Dict[str, Any]) -> None:
        """
        Update the result associated with the given key.

        If the key exists in the results dictionary, update its value
        with the provided new_result.

        Args:
            key (str): The key for the result to be updated.
            new_result (Dict[str, Any]): The new data to update the result.
        """
        if key in self._results:
            self._results[key].update(new_result)

    def delete_result(self, key: str) -> None:
        """
        Delete the result associated with the given key.

        If the key exists in the results dictionary, remove the
        corresponding result.

        Args:
            key (str): The key for the result to be deleted.
        """
        if key in self._results:
            self._results.pop(key, None)


class HunterAPI(CRUDMixin):

    """
    HunterAPI class for interacting with the Hunter.io API.

    Args:
        api_key (str, optional): The API key for Hunter.io. If not provided, a
         default key will be used.

    Attributes:
        _base_url (str): The base URL for Hunter.io API.
        _my_api_key (str): The API key to be used for requests.
    """

    _base_url: str = 'https://api.hunter.io/v2/'
    _my_api_key: str

    def __init__(self, api_key: Optional[str] = None) -> None:
        """
        Initialize the HunterAPI object.

        Args:
            api_key (str, optional): The API key for Hunter.io. If not
            provided, a default key will be used.
        """
        super().__init__()
        self._results = {}
        self._my_api_key = api_key if api_key else (
            '9e66b976c2e357e6fbf'
            '3db75696927dff29000e4'
        )

    async def make_request(self, url: str) -> Dict[str, Any]:
        """
        Make an HTTP request to the provided URL.

        Args:
            url (str): The URL for the HTTP request.

        Returns:
            dict: The JSON response from the API.
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                          '(KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'Accept': '*/*',
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()

    async def verification_email(self, mail: str) -> Dict[str, Any]:
        """
        Verify an email address using the Hunter.io API.

        Args:
            mail (str): The email address to be verified.

        Returns:
            dict: The JSON response from the API.
        """
        url = (
            f'{self._base_url}email-verifier?email='
            f'{mail}&api_key={self._my_api_key}'
        )
        return await self.make_request(url)

    async def get_info_about_account(
            self,
            api_key: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get information about the Hunter.io account.

        Args:
            api_key (str, optional): The API key for Hunter.io. If provided,
             it will override the instance key.

        Returns:
            dict: The JSON response from the API.
        """
        if api_key:
            url = f'{self._base_url}account?api_key={api_key}'
        else:
            url = f'{self._base_url}account?api_key={self._my_api_key}'
        return await self.make_request(url)

    async def search_domain(
            self,
            domain: str,
            company: str,
            limit: Optional[int] = None,
            offset: Optional[int] = None,
            email_type: Optional[str] = None,
            seniority: Optional[str] = None,
            department: Optional[str] = None,
            required_field: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Search for information about a domain using the Hunter.io API.

        Args:
            domain (str): The domain to search.
            company (str): The company name associated with the domain.
            limit (int, optional): The maximum number of results to return.
            offset (int, optional): The number of results to skip.
            email_type (str, optional): Type of email addresses to get
            (personal or generic).
            seniority (str, optional): Seniority level of people to get
            (junior, senior, executive).
            department (str, optional): Department(s) to filter results
            (comma-delimited).
            required_field (str, optional): Required field(s) to filter
            final for (comma-delimited).

        Returns:
            dict: The JSON response from the API.
        """
        request_params: Dict[str, Optional[str, int]] = {
            'domain': domain,
            'company': company,
            'limit': limit,
            'offset': offset,
            'type': email_type,
            'seniority': seniority,
            'department': department,
            'required_field': required_field,
        }

        url = f'{self._base_url}domain-search?'
        url += '&'.join(
            f'{key}={value}'
            for key, value in request_params.items()
            if value is not None
        )
        url += f'&api_key={self._my_api_key}'

        return await self.make_request(url)

    async def email_finder(
            self,
            domain: Optional[str] = None,
            company: Optional[str] = None,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            full_name: Optional[str] = None,
            max_duration: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Find the most likely email address from a domain name, first name.
        And last name using the Hunter.io API.

        Args:
            domain (str, optional): The domain name of the company.
            company (str, optional): The company name from which
            to find email addresses.
            first_name (str, optional): The person's first name.
            last_name (str, optional): The person's last name.
            full_name (str, optional): The person's full name.
            max_duration (int, optional): The maximum duration
            of the request in seconds.

        Returns:
            dict: The JSON response from the API.
        """
        request_params: Dict[str, Optional[str, int]] = {
            'domain': domain,
            'company': company,
            'first_name': first_name,
            'last_name': last_name,
            'full_name': full_name,
            'max_duration': max_duration,
        }

        url = f'{self._base_url}email-finder?'
        url += '&'.join(
            f'{key}={value}'
            for key, value in request_params.items()
            if value is not None
        )
        url += f'&api_key={self._my_api_key}'

        return await self.make_request(url)

    async def get_list_of_lead(self) -> Dict[str, Any]:
        """
        Get a list of leads using the Hunter.io API.

        Returns:
            dict: The JSON response from the API.
        """
        url = f'{self._base_url}leads?api_key={self._my_api_key}'
        return await self.make_request(url)

    async def email_check_service(self, mail: str) -> None:
        """
        Verify an email address using the Hunter.io API.

        Args:
            mail (str): The email address to be verified.

        This method calls the verification_email method to check
        the email address and stores the result using the create_result method.

        Usage example:
        ```python
        await api.email_check_service(mail='example@email.com')
        ```
        """
        result_for_check = await self.verification_email(mail=mail)
        self.create_result('email_check', result_for_check)


async def crud_demonstration():
    """
    Asynchronous function demonstrating the usage of the HunterAPI class.

    - Calls the email_check_service method to verify an email address.
    - Updates the result of the email check with a new status.
    - Deletes the result of the email check.

    Usage example:
    ```python
    asyncio.run(main())
    ```
    """
    await api.email_check_service(mail='example@email.com')
    api.update_result('email_check', {'status': 'updated'})
    api.delete_result('email_check')


if __name__ == '__main__':
    api = HunterAPI()
    info_about_account = asyncio.run(api.get_info_about_account())
    domain_info = asyncio.run(
        api.search_domain(domain='intercom.io', company='Intercom', limit=1)
    )
    print(domain_info)
    verification = asyncio.run(
        api.verification_email(mail='gkarabestkii@gmail.com'),
    )
    print(verification)
    email_finder = asyncio.run(
        api.email_finder(
            domain='reddit.com', first_name='Alexis', last_name='Ohanian',
        ),
    )
    print(email_finder)
    list_of_lead = asyncio.run(api.get_list_of_lead())
    print(asyncio.run(crud_demonstration()))
