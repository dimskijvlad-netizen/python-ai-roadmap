age = int(input("How old you are? "))
english = input("What is your English level? ")
py = int(input("What is your Python level? "))

print("AI CAREER REPORT")

print(f"Age: {age}")
print(f"English level: {english}")
print(f"Python: {py}")

print("\nRecommendations:")

if py < 5:
    print("- Keep learning fundamentals")
elif py < 8:
    print("- Start building projects")
elif py > 7:
    print("- Move to APIs and FastAPI")

if english == 'A1' or english == 'A2':
    print("- Start watching content in English")
elif english == 'B1' or english == 'B2':
    print("- Practice speaking and writing")
elif english == 'C1' or english == 'C2':
    print("- Move to other country")

print("- Build GitHub portfolio ")