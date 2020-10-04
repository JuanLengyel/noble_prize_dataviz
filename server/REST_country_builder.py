import requests

COUNTRY_ROOT_URL = 'https://restcountries.eu/rest/v2'

def make_country_request(mode='all', name=None, params=None, base_url=COUNTRY_ROOT_URL):
    """Function to easily call the REST country (https://restcountries.eu/) REST API

    Args:
        mode (str): The kind of REST query to make to the REST country service.
            Defaults to 'all'.
        name (str): If mode is other than 'all' give a proper name to the query.
            Defaults to None.
        params (dict): A dictionary with key 'fields' and the information to be
            filtered from the query. Defaults to None.
        base_url (str): The base URL for the REST requests

    Returns:
        request.Response: The response from the RESTful service, if the request is successful

    Raises:
        Exception: In case the response status code is different from 200
    """

    if not name:
        name = {}
    
    if not params:
        params = {}

    if mode == 'all':
        print(f'{base_url}/{mode}')
        response = requests.get(f'{base_url}/{mode}')
    else:
        response = requests.get(f'{base_url}/{mode}/{name}', params)

    if not response.status_code == 200:
        raise Exception(f'Request failed with status code {response.status_code}')

    return response