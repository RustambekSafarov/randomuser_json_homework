from from_json import read_json
def get_users(data:dict)->list:
    """Gets a list of users from the data

    Args:
        data (dict): The data from the JSON file

    Returns:
        list: A list of users
    """
    # Get the list of users
    l = []
    for i in data['users']:
        l.append(i)
    return l


data = read_json("users.json")
print(get_users(data))