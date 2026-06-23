topics_count = int(input("How many topics did you learn today? "))
topics = []
print("Enter each topic: ")
for i in range(1, topics_count + 1):
    topic = input(f"Topic {i}: ")
    topics.append(topic)
print("\nTODAY'S LEARNING")
for topic in topics:
    print(f"- {topic}")