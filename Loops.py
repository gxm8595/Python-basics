# while loops = a statement that will execute it's block of code,
#               as long as it's condition remains true
# name = ""
# while len(name)==0 :
#     name = input("Enter your name : ")
# print("Hello "+ name)

# We can use the same thing here as well.


# name = None
# while not name :
#     name = input("Enter your name : ")
# print("Hello "+ name)

#  For loops

#  for loops  : a statement that will execute it's block of code
#               a limited amount of times
#
#               while loop = unlimited
#               for loop = limited

# for a in range(11):
#     print(a+1)

# for a in range(20,50+1,4):
#     print(a)

# for s in "Hello World ":
#     print(s)


# import time
# for ab in range(10,0,-1):
#     print(ab)
#     time.sleep(2)
# print("My name is Gxm")


# nested loop : The "inner loop" will finish all of it's iterationbefore finishing one iteration
#               of the "outer loop"

# rows = int(input("Enter no of rows :"))
# column = int(input("Enter no of column :"))
# signs = input("Enter your sign : ")
#
# for a in range(rows):
#     for b in range(column):
#         print(signs, end="")
#     print()
#
# loop Control statements = change a loop execution from its normal sequence
# break =    used to termenate the loop entirely
# continue = skips to the next iteration of the loop.
# pass =     does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name")
#     if name != "":
#         break
# print("Hello " + name)
#
# phone_number = "012-345-6789"
# for i in phone_number:
#     if i == "-" :
#         continue
#     print(i, end="")

# for i in range(1,16):
#     if i == 13 :
#         pass
#     else:
#         print(i, )