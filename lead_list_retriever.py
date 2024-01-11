"""
Module providing a LeadListRetriever for retrieving lists of leads from an API.

This module includes a class, LeadListRetriever, which utilizes,
the AsyncHttpRequestor.
to make asynchronous requests to an API for fetching lists of leads.
"""
from typing import Any, Dict

from http_requestor import AsyncHttpRequestor
from url_utils import build_url


class LeadListRetriever(object):
    """
    A class for retrieving lists of leads from an API.

    Args:
        base_url (str): The base URL for the API to use.
        my_api_key (str): The API key to be used for requests.

    Attributes:
        base_url (str): The base URL for the API.
        my_api_key (str): The API key to be used for requests.
    """

    def __init__(self, base_url: str, my_api_key: str) -> None:
        """
        Initialize the LeadListRetriever object.

        Args:
            base_url (str): The base URL for the API to use.
            my_api_key (str): The API key to be used for requests.
        """
        self.base_url = base_url
        self.my_api_key = my_api_key

    async def get_list_of_lead(self) -> Dict[str, Any]:
        """
        Retrieve a list of leads from the API.

        Returns:
            Dict[str, Any]: The JSON response from the API,
                containing the list of leads.
        """
        url = build_url(self.base_url, 'leads', api_key=self.my_api_key)

        return await AsyncHttpRequestor().make_request(url)
