studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]
for name in studentNames:
    print(name + " Evans")

new = input("Add name: ")
studentNames.append(new)
for name in studentNames:
    print(name + " Evans")
