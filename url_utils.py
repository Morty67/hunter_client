"""A module that provides a function for building URLs for API requests.

This module contains the `build_url` function, which builds a URL by combining
the base API URL, endpoint, and optional request parameters.
"""

from urllib.parse import urlencode


def build_url(base_url: str, endpoint: str, **kwargs) -> str:
    """
    Construct a URL for an API request.

    Args:
        base_url (str): The base URL of the API.
        endpoint (str): The specific endpoint to target.
        kwargs: Additional query parameters to include in the URL.

    Returns:
        str: The constructed URL.
    """
    url_segments = [base_url, endpoint]
    if kwargs:
        query_params = urlencode(kwargs)
        url_segments.append('?{}'.format(query_params))
    return ''.join(url_segments)
