import requests
def get_username():
    username = input("Enter your username: ")
    return username
def get_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200: return response.json()
    else: return None
def print_user_data(data):
    print(f"\nName:{data['name']}")
    print(f"Login:{data['login']}")
    print(f"Public repositories:{data['public_repos']}")
data = get_user_data(get_username())
if data: print_user_data(data)
else: print("User not found")
