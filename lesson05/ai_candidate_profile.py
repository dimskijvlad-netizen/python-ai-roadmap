def get_user_data():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    english = input("Enter your English level: ")
    python_level = input("Enter your your Python level: ")
    return name, age, english, python_level
def save_in_dictionary(name,age,english,python_level):
    dictionary = {
    "name": name,
    "age": age,
    "english": english,
    "python_level": python_level
    }
    return dictionary
def print_profile(dictionary):
    print("\nAI CANDIDATE PROFILE\n")
    
    print(f"Name: {dictionary['name']}")
    print(f"Age: {dictionary['age']}")
    print(f"English: {dictionary['english']}")
    print(f"Python: {dictionary['python_level']}")
    print(f"\nTotal fields: {len(dictionary)}")
print_profile(save_in_dictionary(*get_user_data()))