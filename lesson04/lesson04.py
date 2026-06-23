skills = []
skills_count = int(input("How many skills do you have? "))
print("\nEnter your skills:")
for i in range(skills_count):
    skill = input("")
    skills.append(skill)
print("YOUR AI SKILLS:\n")
for i in range(skills_count):
    print(f"{i + 1}. {skills[i]} ")

print(f"Total skills: {skills_count}")
if 'Python' in skills:
    print("Python detected")
else: print("Learn Python first")