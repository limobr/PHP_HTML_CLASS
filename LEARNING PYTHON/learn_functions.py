#Creating a function
def php_function():
    print('Hello php class students')

# php_function()

# -----sum of two numbers----
def calcSum():
    global num1
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print(f"The sum of two numbers is {num1 + num2}")

# calcSum()
# print(f"The first number is {num1}.")
name = input("Enter your name: ")
age = input("\nEnter your age: ")
gender = input("\nEnter your gender: ")
def personal_details(name, age, gender):
    print(f"Hello {name}, your gender is {gender} and your age is {age}")

personal_details(name, age, gender)  