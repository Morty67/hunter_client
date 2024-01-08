"""Module with CRUD demonstration function."""

from typing import Any, Dict


async def crud_demonstration(api: Any) -> Dict[str, Any]:
    """
    Demonstrate CRUD functionality.

    Args:
        api (Any): An instance of the HunterAPI class.

    Returns:
        dict: A dictionary containing demonstration results.
    """
    demo_results = {}
    # Demonstration of the email_check_service function
    await api.email_check_service(mail='example@email.com')
    # Demonstration of CRUD functionality
    key = 'email_check'
    # Save all results in a dictionary
    demo_results['create'] = api.read_result(key)
    # Update the result
    new_result = {'status': 'verified'}
    api.update_result(key, new_result)
    demo_results['update'] = api.read_result(key)
    # Deleting a result
    api.delete_result(key)
    demo_results['delete'] = api.read_result(key)
    return demo_results
