"""
Module providing an AccountInfoRetriever for fetching information from Hunter.

This module includes a class, AccountInfoRetriever, which utilizes,
the AsyncHttpRequestor
to make asynchronous requests to the Hunter.io API for retrieving, account
information.
"""

from typing import Any, Dict, Optional

from http_requestor import AsyncHttpRequestor
from url_utils import build_url


class AccountInfoRetriever(object):
    """
    A class for retrieving information about a Hunter.io account.

    Args:
        base_url (str): The base URL for the Hunter.io API.
        my_api_key (str): The API key to be used for requests.

    Attributes:
        base_url (str): The base URL for the Hunter.io API.
        my_api_key (str): The API key to be used for requests.
    """

    def __init__(self, base_url: str, my_api_key: str) -> None:
        """
        Initialize the AccountInfoRetriever object.

        Args:
            base_url (str): The base URL for the Hunter.io API.
            my_api_key (str): The API key to be used for requests.
        """
        self.base_url = base_url
        self.my_api_key = my_api_key

    async def get_info_about_account(
        self, api_key: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Get information about the Hunter.io account.

        Args:
            api_key (str, optional): The API key for Hunter.io. If provided,
                it will override the instance key.

        Returns:
            dict: The JSON response from the API containing information,
                about the account.
        """
        url = build_url(
            self.base_url, 'account', api_key=api_key or self.my_api_key,
        )
        return await AsyncHttpRequestor().make_request(url)
