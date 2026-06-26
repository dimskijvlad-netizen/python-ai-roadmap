def get_candidate():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    english = input("Enter your English level: ")
    dictionary = {
        'name': name,
        'age': age,
        'english': english
    }
    return dictionary