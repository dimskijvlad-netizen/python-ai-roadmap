import json
def get_user_data():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    english = input("Enter your English level: ")
    python_level = input("Enter your Python level: ")
    return name, age, english, python_level
def save_in_dictionary(name, age, english, python_level):
    dictionary = {
        "name": name,
        "age": age,
        "english": english,
        "python_level": python_level
    }
    return dictionary
def convert_to_json(dictionary):
    json_data = json.dumps(dictionary,indent=4)
    return json_data
print(convert_to_json(save_in_dictionary(*get_user_data())))
