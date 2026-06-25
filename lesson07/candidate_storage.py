from json import dumps
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
        "python level": python_level
    }
    return dictionary
def convert_to_json(dictionary):
    json_data = dumps(dictionary,indent=4)
    return json_data
def write_in_file(json_data):
    with open("candidate.json","w") as file:
        file.write(json_data)
    return file
def read_file(file):
    with open("candidate.json","r") as file:
        readf = file.read()
    return readf
print(read_file(write_in_file(convert_to_json(save_in_dictionary(*get_user_data())))))