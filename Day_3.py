name = input("Enter your name: ")

print("Welcome", name)

tasks = [
    "Review supplier report",
    "Prepare KPI dashboard",
    "Check ISO requirements"
]

print("Today's Tasks:")

for task in tasks:
    print("-", task)