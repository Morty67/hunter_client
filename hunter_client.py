"""Module providing the HunterAPI for interacting with the Hunter.io API.

This module defines the HunterAPI class, which serves as a client,
for interacting with the Hunter.io API. It encapsulates various
functionalities, for email verification, account information retrieval,
domain searching, email finding, and lead list retrieval.

Classes:
    - HunterAPI: Main class for interacting with the Hunter.io API.
"""

import asyncio
from typing import Any, Dict, Optional

from account_info_retriever import AccountInfoRetriever
from crud_mixin import CRUDMixin
from demonstration_utils import crud_demonstration
from email_finder import EmailFinder
from email_verifer import EmailVerifier
from lead_list_retriever import LeadListRetriever


class HunterAPI(CRUDMixin):
    """Client for interacting with the Hunter.io API.

    This class encapsulates functionalities for interacting with various
         endpoints of the Hunter.io API, including email verification,
         account information retrieval, domain searching, email finding,
         and lead list retrieval.

    Attributes:
        - _base_url (str): The base URL for the Hunter.io API.
        - _my_api_key (str): The API key used for authentication.
    """

    def __init__(self, api_key: Optional[str] = None) -> None:
        """
        Initialize the HunterAPI object.

        Args:
            api_key (str, optional): API key for Hunter.io. If not provided,
                a default key will be used.
        """
        super().__init__()
        self._base_url = 'https://api.hunter.io/v2/'
        self._my_api_key = (
            api_key
            if api_key
            else ('9e66b976c2e357e6fbf3db75696927dff29000e4')
        )
        self.email_verifier = EmailVerifier(self._base_url, self._my_api_key)
        self.account_info_retriever = AccountInfoRetriever(
            self._base_url, self._my_api_key,
        )
        self.email_finder = EmailFinder(self._base_url, self._my_api_key)
        self.lead_list_retriever = LeadListRetriever(
            self._base_url, self._my_api_key,
        )

    async def email_check_service(self, mail: str) -> Dict[str, Any]:
        """
        Service for email checking.

        This method provides a service for checking an email address.
        Replace the placeholder implementation with your actual logic.

        Args:
            mail (str): The email address to be checked.

        Returns:
            dict: The result of the email checking service.
        """
        result_for_check = {'status': 'checked', 'mail': mail}
        self.create_result('email_check', result_for_check)
        return result_for_check

    async def verification_email(self, mail: str) -> Dict[str, Any]:
        """
        Verify an email address using the Hunter.io API.

        Args:
            mail (str): The email address to be verified.

        Returns:
            dict: The result of the email verification.
        """
        return await self.email_verifier.verification_email(mail)

    async def get_info_about_account(
        self, api_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Get information about the Hunter.io account.

        Args:
            api_key (str, optional): The API key for Hunter.io. If provided,
                it will override the instance key.

        Returns:
            dict: The result of the account information retrieval.
        """
        return await self.account_info_retriever.get_info_about_account(
            api_key,
        )

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
            dict: The result of the email finding.
        """
        return await self.email_finder.email_finder(
            domain, company, first_name, last_name,
        )

    async def get_list_of_lead(self) -> Dict[str, Any]:
        """
        Get a list of leads using the Hunter.io API.

        Returns:
            dict: The result of the lead list retrieval.
        """
        return await self.lead_list_retriever.get_list_of_lead()


if __name__ == '__main__':
    api = HunterAPI()
    # Call email_check_service before CRUD demonstration
    asyncio.run(api.email_check_service(mail='example@email.com'))

    verification_result = asyncio.run(api.email_verifier.verification_email(
        mail='gkarabestkii@gmail.com',
    ))
    account_info_result = asyncio.run(
        api.account_info_retriever.get_info_about_account(),
    )
    email_finder_result = asyncio.run(api.email_finder.email_finder(
        domain='reddit.com',
        first_name='Alexis',
        last_name='Ohanian',
    ))
    lead_list_result = asyncio.run(api.lead_list_retriever.get_list_of_lead())

    # Demonstrates CRUD operations
    crud_results = asyncio.run(crud_demonstration(api))
