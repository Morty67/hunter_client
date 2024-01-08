"""Module with AsyncHttpRequestor for making asynchronous HTTP requests."""

from typing import Any, Dict

import httpx


class AsyncHttpRequestor(object):
    """A basic async HTTP client for making requests."""

    async def make_request(self, url: str) -> Dict[str, Any]:
        """
        Make an HTTP request to the provided URL.

        Args:
            url (str): The URL for the HTTP request.

        Returns:
            dict: The JSON response from the API.
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
