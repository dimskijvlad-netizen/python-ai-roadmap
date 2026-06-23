def get_user_data():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    english = input("Enter your English level: ")
    python = input("Enter your Python level: ")
    user_data = []
    user_data.append(name)
    user_data.append(age)
    user_data.append(english)
    user_data.append(python)
    return user_data
def generate_profile(user_data):
    generated_profile = []
    name = user_data[0]
    age = user_data[1]
    if user_data[2] == 'A1' or user_data[2] == 'A2': user_data[2] = 'Beginner'
    elif user_data[2] == 'B1' or user_data[2] == 'B2': user_data[2] = 'Independent'
    else: user_data[2] = 'Advanced'
    if user_data[3] == 'A1' or user_data[3] == 'A2': user_data[3] = 'Beginner'
    elif user_data[3] == 'B1' or user_data[3] == 'B2': user_data[3] = 'Independent'
    elif user_data[3] == 'C1': user_data[3] = 'Advanced'
    else: user_data[3] = 'Expert'
    for item in user_data:
        generated_profile.append(item)
    return generated_profile
def print_profile(generated_profile):
    user_data = generated_profile
    print("\n**********************")
    print("AI Profile Generator")
    print("**********************\n")

    print(f"Name: {user_data[0]}")
    print(f"Age: {user_data[1]}")
    print(f"English level: {user_data[2]}")
    print(f"Python level: {user_data[3]}")

print_profile(generate_profile(get_user_data()))