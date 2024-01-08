## Hunter.io API Client
This Python module serves as a client for interacting with the Hunter.io API. It provides a convenient wrapper for performing tasks such as email verification, domain search, email finding, and more. The asynchronous client, HunterAPI, exposes methods corresponding to different API endpoints.

## Installing / Getting started:
```shell
To get started, you need to clone the repository from GitHub: https://github.com/Morty67/hunter_client/tree/developer
Python 3.11.3 must be installed

python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)

pip install -r requirements.txt
```


## Methods:
*  verification_email: Verify an email address using the Hunter.io API.
*  get_info_about_account: Get information about the Hunter.io account.
*  search_domain: Search for information about a domain using the Hunter.io API.
*  email_finder: Find the most likely email address from a domain name, first name, and last name using the Hunter.io API.
*  get_list_of_lead: Get a list of leads using the Hunter.io API.
*  email_check_service: Verify an email address using the Hunter.io API. This method stores the result using the CRUD operations.

## Asynchronous CRUD Demonstration
The crud_demonstration function demonstrates the usage of the asynchronous CRUD operations:

*  Calls the email_check_service method to verify an email address.
*  Updates the result of the email check with a new status.
*  Deletes the result of the email check.

## Docker Integration 🐳
*  To run the project using Docker, you can use the provided Dockerfile. Build and run the Docker container as follows:
*  docker build -t hunter-client .
*  docker run hunter-client
