import requests
def get_username():
    username = input("Enter username: ")
    return username
def get_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    if response.status_code == 200: return response.json(), 1
    elif response.status_code == 404: return response.json(), 2
    else: return None, 0
def print_profile(data,flag):
    if flag == 1:
        print(f"\nName: {data['name']}")
        print(f"Login: {data['login']}")
        print(f"Public repos: {data['public_repos']}")
        print(f"Followers: {data['followers']}")
        print(f"Following: {data['following']}")
        print(f"Account created: {data['created_at']}")
    elif flag == 2:
        print("User not found")
    else: print("Network error")
print_profile(*get_user_data(get_username()))


