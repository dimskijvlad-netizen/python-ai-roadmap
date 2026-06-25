import requests
def get_username():
    username = input("Enter your username: ")
    return username
def get_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    data = response.json()
    return data
def print_user_data(data):
    print(f"\nName:{data['name']}")
    print(f"Login:{data['login']}")
    print(f"Public repositories:{data['public_repos']}")
print_user_data(get_user_data(get_username()))
