"""Module providing a HunterAPI for interacting with the Hunter.io API."""

import asyncio
from typing import Any, Dict, Optional

from http_requestor import AsyncHttpRequestor
from crud_mixin import CRUDMixin
from demonstration_utils import crud_demonstration


class HunterAPI(AsyncHttpRequestor, CRUDMixin):
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
            api_key (str, optional): API key for Hunter.io. If not provided,
                a default key will be used.
        """
        super().__init__()
        self._query_results = {}
        self._my_api_key = api_key if api_key else (
            '9e66b976c2e357e6fbf' +
            '3db75696927dff29000e4'
        )

    async def verification_email(self, mail: str) -> Dict[str, Any]:
        """
        Verify an email address using the Hunter.io API.

        Args:
            mail (str): The email address to be verified.

        Returns:
            dict: The JSON response from the API.
        """
        url = '{0}email-verifier?email={1}&api_key={2}'.format(
            self._base_url, mail, self._my_api_key,
        )
        return await self.make_request(url)

    async def get_info_about_account(
        self,
        api_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Get information about the Hunter.io account.

        Args:
            api_key (str, optional): The API key for Hunter.io. If provided,
                it will override the instance key.

        Returns:
            dict: The JSON response from the API.
        """
        url = '{0}account?api_key={1}'.format(
            self._base_url,
            api_key or self._my_api_key,
        )
        return await self.make_request(url)

    async def search_domain(
        self,
        domain: str,
        company: str,
        limit: Optional[int] = None,
        email_type: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Search for information about a domain using the Hunter.io API.

        Args:
            domain (str): The domain to search.
            company (str): The company name associated with the domain.
            limit (int, optional): The maximum number of results to return.
            email_type (str, optional): Type of email addresses to get.

        Returns:
            dict: The JSON response from the API.
        """
        request_params: Dict[str, Optional[str, int]] = {
            'domain': domain,
            'company': company,
            'limit': limit,
            'type': email_type,
        }

        url = '{0}domain-search?{1}&api_key={2}'.format(
            self._base_url,
            '&'.join(
                '{0}={1}'.format(key, param_value)
                for key, param_value in request_params.items()
                if param_value is not None
            ),
            self._my_api_key,
        )
        url += '&api_key={0}'.format(self._my_api_key)
        return await self.make_request(url)

    async def email_finder(
        self,
        domain: Optional[str] = None,
        company: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Find the most likely email address from a domain name.

        Args:
            domain (str, optional): The domain name of the company.
            company (str, optional): The company name from which to find email.
            first_name (str, optional): The person's first name.
            last_name (str, optional): The person's last name.

        Returns:
            dict: The JSON response from the API.
        """
        request_params: Dict[str, Optional[str, int]] = {
            'domain': domain,
            'company': company,
            'first_name': first_name,
            'last_name': last_name,
        }

        url = '{0}email-finder?{1}&api_key={2}'.format(
            self._base_url,
            '&'.join(
                '{0}={1}'.format(key, param_value)
                for key, param_value in request_params.items()
                if param_value is not None
            ),
            self._my_api_key,
        )
        return await self.make_request(url)

    async def get_list_of_lead(self) -> Dict[str, Any]:
        """
        Get a list of leads using the Hunter.io API.

        Returns:
            dict: The JSON response from the API.
        """
        url = '{0}leads?api_key={1}'.format(self._base_url, self._my_api_key)
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


if __name__ == '__main__':
    api = HunterAPI()
    info_about_account = asyncio.run(api.get_info_about_account())
    domain_info = asyncio.run(
        api.search_domain(domain='intercom.io', company='Intercom', limit=1),
    )
    verification = asyncio.run(
        api.verification_email(mail='gkarabestkii@gmail.com'),
    )
    email_finder = asyncio.run(
        api.email_finder(
            domain='reddit.com', first_name='Alexis', last_name='Ohanian',
        ),
    )
    list_of_lead = asyncio.run(api.get_list_of_lead())
    asyncio.run(crud_demonstration(api))
