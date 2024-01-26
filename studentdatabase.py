names = ['Nita', 'Jimin', 'Raina', 'Namjoon']
favorite_food = ('oyakodon', 'Chicken Tikka Masala', 'Katsudon', 'Unagidon')
home_town = ('Tokyo', 'Bussan', 'Osaka', 'Detroit')

def students(names, home_town, favorite_food):
    if 0 <= greeting - 1 < len(names):
        print(f"Student {names[greeting - 1]}. What would you like to know about this student?")
        response = input('Enter "hometown" or "favorite food": ')
        if response == "hometown":
            print(f"{names[greeting - 1]}'s hometown is {home_town[greeting - 1]}.")
        elif response == "favorite food":
            print(f"{names[greeting - 1]}'s favorite food is {favorite_food[greeting - 1]}.")
        else:
            print("Invalid response. Please try again.")

while True:
    try:
        greeting = int(input("Welcome! Which student would you like to learn more about? Enter a number 1-4 (Enter 0 to exit): "))
        if greeting == 0:
            break
        students(names, home_town, favorite_food)
    except ValueError:
        print("Invalid entry. Please enter a valid number.")