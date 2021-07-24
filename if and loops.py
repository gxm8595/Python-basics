# if statement = a block of code that will execute if it's condition is true

# age = int(input("Enter your age :"))
# if age >=100:
#     print("You are going to die soon!")
# if age == 18:
#     print("Congrats, you just became an adult!")
# if age > 18 > 100:
#     print("You are going to die soon!")
# if age < 100:
#     print("You are already an adult!")
# else:
#     print("Enter valid number")


# logical operators(and, or, not) = used to check if two or more conditional statements are true.
temp = int(input("What is the temperature outside? : "))
# if temp >= 0 and temp <= 30:
#     print("The temperature is good today! ")
#     print("You can go outside! ")
#
#
# elif temp < 0  or temp > 30 :
#     print("The temperature is bad today! ")
#     print("You should stay in home")

# elif temp >= 30 or temp <= 100:
#     print("The temperature is bad today! ")
#     print("You should stay in home")

          # not logical operator
if not(temp >= 0 and temp <= 30):
    print("The temperature is good today! ")
    print("You can go outside! ")


elif not(temp < 0  or temp > 30) :
    print("The temperature is bad today! ")
    print("You should stay in home")






