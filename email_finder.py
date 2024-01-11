"""
Module providing an EmailFinder for finding email addresses using an API.

This module include class, EmailFinder, which utilizes the AsyncHttpRequestor.
to make asynchronous requests to an API for finding email addresses based on
provided criteria.
"""
from typing import Any, Dict, Optional

from http_requestor import AsyncHttpRequestor
from url_utils import build_url


class EmailFinder(object):
    """
    A class for finding email addresses using an API.

    Args:
        base_url (str): The base URL for the API to use.
        my_api_key (str): The API key to be used for requests.

    Attributes:
        base_url (str): The base URL for the API.
        my_api_key (str): The API key to be used for requests.
    """

    def __init__(self, base_url: str, my_api_key: str) -> None:
        """
        Initialize the EmailFinder object.

        Args:
            base_url (str): The base URL for the API.
            my_api_key (str): The API key to be used for requests.
        """
        self.base_url = base_url
        self.my_api_key = my_api_key

    async def email_finder(
        self,
        domain: Optional[str] = None,
        company: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Find email addresses using the API.

        Args:
            domain (str, optional): The domain to search.
            company (str, optional): The company name associated with email.
            first_name (str, optional): The first name of the person to find.
            last_name (str, optional): The last name of the person to find.

        Returns:
            Dict[str, Any]: The JSON response from the API, containing, the
                found email addresses.
        """
        url = build_url(
            self.base_url,
            'email-finder',
            domain=domain,
            company=company,
            first_name=first_name,
            last_name=last_name,
            api_key=self.my_api_key,
        )
        return await AsyncHttpRequestor().make_request(url)
