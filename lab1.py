def calculate_age():
    try:
        user_input = int(input("Enter the birth year: "))
        age = 2024 - user_input
        print("Your age is: {}" .format(age))
    except ValueError:
        print("Please enter a valid integer for the birth year.")

calculate_age()

def helloWorld():
    print('Hello World')

helloWorld()
