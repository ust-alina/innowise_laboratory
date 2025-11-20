def generate_profile(age: int):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19: 
        return "Teenager"
    elif age >= 20: 
        return "Adult"
    else:
        return "Age not found"

user_name = input("Hi! Enter your full name: ")
birth_year_str = input("Enter your birth year: ")

if not birth_year_str.isdigit():
    print("Error! Not number")
    birth_year_str = input("Enter your birth year: ")
elif int(birth_year_str) < 1900:
    sure_year = input(f"Are you sure? Your birth year {birth_year_str}? Type yes or no: ")
    if sure_year == 'no':
        birth_year_str = input("Enter your birth year: ")
    elif sure_year == 'yes':
        print("Ok")
    else:
        print("Command not recognized")
        birth_year_str = input("Enter your birth year: ")

birth_year = int(birth_year_str)

current_age = 2025 - birth_year

hobbies = []
hobby = input("Enter a favorite hobby or type 'stop' to finish: ")

while hobby.lower() != 'stop':
    hobbies.append(hobby)
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")


life_stage = generate_profile(current_age)


user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

print("---")
print("Profile Summary:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")

if len(hobbies) == 0:
   print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(hobbies)}):")
    for hobby in hobbies:
        print(f"- {hobby}")
print("---")
