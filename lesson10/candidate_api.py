import requests
def get_candidate_data():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    english = input("Enter your English level: ")
    desired_role = input("Enter your desired role: ")
    return name, age, english, desired_role
def create_candidate(name, age, english, desired_role):
    candidate = {
        "name": name,
        "age": age,
        "english": english,
        "desired_role": desired_role
    }
    return candidate
def send_candidate(candidate):
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json = candidate)
    if response.status_code == 201: return response
    else: return None
def print_response(response):
    if response is None: print("Request failed")
    else:
        data = response.json()
        print("\n",data)
        print("\nCandidate successfully sent")
        print(f"\nID: {data['id']}")
        print(f"Name: {data['name']}")
        print(f"Role: {data['desired_role']}")

print_response(send_candidate(create_candidate(*get_candidate_data())))