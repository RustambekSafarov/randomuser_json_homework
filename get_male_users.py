from from_json import read_json
def get_male_users(data:dict)->list:
    """Gets all male users from the data
    Args:
        data (dict): The data from the JSON file
    Returns:
        list: A list of users
    """
    l = []
    for i in data['users']:
        if i['gender']=='male':
            l.append(i['name'])
            
    return l
data = read_json("users.json")
print(get_male_users(data))