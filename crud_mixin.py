"""Module providing a CRUD (Create, Read, Update, Delete) mixin class."""

from typing import Any, Dict, Optional


class CRUDMixin(object):
    """
    Mixin class providing basic CRUD (Create, Read, Update, Delete) operations.

    Attributes:
        _results_for_crud (Dict[str, Any]): A dictionary to store results.
    """

    def __init__(self) -> None:
        """Initialize the CRUDMixin object."""
        self._results_for_crud = {}

    def create_result(self, key: str, result_data: Dict[str, Any]) -> None:
        """
        Create a new result and store it in the _results dictionary.

        Args:
            key (str): The key to identify the result.
            result_data (Dict[str, Any]): The result to be stored.
        """
        self._results_for_crud[key] = result_data

    def read_result(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Read and return a result from the _results dictionary.

        Args:
            key (str): The key to identify the result.

        Returns:
            Optional[Dict[str, Any]]: The result associated with the key,
             or None if not found.
        """
        return self._results_for_crud.get(key)

    def update_result(self, key: str, new_result: Dict[str, Any]) -> None:
        """
        Update an existing result in the _results dictionary.

        Args:
            key (str): The key to identify the result to be updated.
            new_result (Dict[str, Any]):The new result to replace the existing.
        """
        existing_result = self._results_for_crud.get(key)

        if existing_result is not None:
            existing_result.update(new_result)
            self._results_for_crud[key] = existing_result.copy()

    def delete_result(self, key: str) -> None:
        """
        Delete a result from the _results dictionary.

        Args:
            key (str): The key to identify the result to be deleted.
        """
        self._results_for_crud.pop(key, None)
