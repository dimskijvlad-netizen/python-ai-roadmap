def get_candidate_data():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        english = input("Enter your English level: ")
        return name, age, english
    except ValueError: 
        print("Age must be a number ")
        return None, None, None
def print_candidate_validation(name, age, english):
    if name is not None: 
        print("\nCandidate validated successfully")
        print(f"\nName: {name}")
        print(f"Age: {age}")
        print(f"English: {english}")
    else: print("Candidate validation failed")
print_candidate_validation(*get_candidate_data())
