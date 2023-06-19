import time
import random

spe = ["@", "#", "!", "?", "_"]

def gen():
    fname = input("First name: ")
    lname = input("Last name: ")
    birthyear = input("Birth year: ")

    # Check if any of the input values are empty
    if not fname or not lname or not birthyear:
        print("Please provide all the required information.")
        return

    print("Generating password...")
    time.sleep(3)

    # Additional inputs for password customization
    length = int(input("Desired password length: "))
    use_special = input("Include special characters? (yes/no): ").lower() == "yes"

    lul = fname.upper()[0]
    ha = birthyear[-2:]
    random_spe = random.choice(spe) if use_special else ""

    suggestions = []
    suggestions.append(lul + random_spe + lname + ha)
    suggestions.append(lname + ha + random_spe + lul)
    suggestions.append(ha + random_spe + lname + lul)
    suggestions.append(lname + lul + ha + random_spe)
    suggestions.append(lul + lname + random_spe + ha)
    suggestions.append(lname + random_spe + lul + ha)
    suggestions.append(ha + lul + random_spe + lname)
    suggestions.append(random_spe + lname + lul + ha)
    suggestions.append(random_spe + lul + ha + lname)
    suggestions.append(lname + random_spe + ha + lul)

    print("Suggestions:")
    for i, suggestion in enumerate(suggestions, start=1):
        if len(suggestion) >= length:
            print(f"{i}. {suggestion[:length]}")
        else:
            print(f"{i}. {suggestion}")

print("Password Generator")
print("Would you like to generate?")
while True:
    option = input("yes or no: ").lower()
    if option == "yes":
        gen()
    elif option == "no":
        break
    else:
        print("Invalid option. Please choose yes or no")
