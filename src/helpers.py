import requests


def convert_to_array_of_dicts(data):
    array_of_dicts = []
    keys = data[0] if data else []
    for row in data[1:]:
        row_dict = {}
        for i, cell in enumerate(row):
            if cell:
                row_dict[keys[i]] = cell
        array_of_dicts.append(row_dict)
    return array_of_dicts


def get_all_values(dictionary):
    return [v for v in dictionary.values()]


def getPlaceId(place):
    if place > 4:
        if place == 5:
            return 6
        else:
            if place == 6:
                return 7
            else:
                return 5
    else:
        return place


def response_exception(response):
    """
    Expanded exception for request
    :param response: Response from API request
    :return: Exception
    """
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
        print(f"Response content: {response.content}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        print(f"Response content: {response.content}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        print(f"Response content: {response.content}")
    except requests.exceptions.JSONDecodeError as errj:
        print(f"Timeout Error: {errj}")
        print(f"Response content: {response.content}")
    except requests.exceptions.RequestException as err:
        print(f"Something Else: {err}")
        print(f"Response content: {response.content}")
