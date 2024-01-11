"""
Module providing an EmailVerifier for verifying email addresses using an API.

This module includes a class, EmailVerifier, which utilizes AsyncHttpRequestor,
to make asynchronous requests to an API for verifying the validity of email.
"""
from typing import Any, Dict

from http_requestor import AsyncHttpRequestor
from url_utils import build_url


class EmailVerifier(object):
    """
    A class for verifying email addresses using an API.

    Args:
        base_url (str): The base URL for the API to use.
        my_api_key (str): The API key to be used for requests.

    Attributes:
        base_url (str): The base URL for the API.
        my_api_key (str): The API key to be used for requests.
    """

    def __init__(self, base_url: str, my_api_key: str) -> None:
        """
        Initialize the EmailVerifier object.

        Args:
            base_url (str): The base URL for the API.
            my_api_key (str): The API key to be used for requests.
        """
        self.base_url = base_url
        self.my_api_key = my_api_key

    async def verification_email(self, mail: str) -> Dict[str, Any]:
        """
        Verify an email address using the API.

        Args:
            mail (str): The email address to verify.

        Returns:
            Dict[str, Any]: The JSON response from the API containing,
                information about the validity of the email address.
        """
        url = build_url(self.base_url, 'email-verifier', email=mail, api_key=self.my_api_key)
        return await AsyncHttpRequestor().make_request(url)
