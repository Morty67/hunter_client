"""Module providing the HunterAPI for interacting with the Hunter.io API.

This module defines the HunterAPI class, which serves as a client,
for interacting with the Hunter.io API. It encapsulates various
functionalities, for email verification, account information retrieval,
domain searching, email finding, and lead list retrieval.

Classes:
    - HunterAPI: Main class for interacting with the Hunter.io API.
"""

import asyncio
from typing import Optional

from account_info_retriever import AccountInfoRetriever
from crud_mixin import CRUDMixin
from demonstration_utils import crud_demonstration
from email_check_service import EmailCheckService
from email_finder import EmailFinder
from email_verifer import EmailVerifier
from lead_list_retriever import LeadListRetriever


class HunterAPI(CRUDMixin):
    """
    Client for interacting with the Hunter.io API.

    This class encapsulates functionalities for interacting with various
         endpoints of the Hunter.io API, including email verification,
         account information retrieval, domain searching, email finding,
         and lead list retrieval.

    Attributes:
        - _base_url (str): The base URL for the Hunter.io API.
        - _my_api_key (str): The API key used for authentication.
        - email_verifier (EmailVerifier): Instance for email verification.
        - account_info_retriever (AccountInfoRetriever): Instance for,
            account, information retrieval.
        - email_finder (EmailFinder): Instance for email finding.
        - lead_list_retriever (LeadListRetriever): Instance for lead, list
            retrieval.
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
        self.email_check_service_instance = EmailCheckService()


if __name__ == '__main__':
    api = HunterAPI()
    # Call email_check_service before CRUD demonstration
    email_check_result = asyncio.run(
        api.email_check_service_instance.check_email(
            mail='gkarabetskii@gmail.com',
        ),
    )
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
