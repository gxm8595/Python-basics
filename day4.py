# # # **kwargs = parameter that will pack all arguments into a dictionary
# # #            useful so that a function can accept a varying amount of keyboard arguments
# #
# # def hello(**kill):
# #     print("Hello",end=" ")
# #     for key,value in kill.items():
# #         print(value,end=" ")
# #
# # hello(title="Mr.",first="Gaurav",middle="Kumar",last="Sharma")
#
#
# # string Format = optional method that gives users more control
# #                 when displaying output
#
# animal = "cow"
# item = "moon"
# # print("The "+ animal + " jumped over the "+ item)
# print("The {} jumped over the {}".format("animal", "item"))
# print("The {} jumped over the {}".format("animal", "item")) # positional argument
# print("The {} jumped over the and th")

#
# import random
# x = random.randint(1,6)
# print(x)
# y= random.random()
#
# myList = ['Hello','Guy', 'Namaste']
# z= random.choice(myList)
# cards = [1,2,3,4,5,6,'j','k']
# random.shuffle(cards)
# print(cards)




# exception = events dectected during execution that interrupt the flow of a program
# try:
#     numerator = int(input("Enter a number to divide:"))
#     denominator = int(input("Enter a number to divide by :"))
#     result = numerator/denominator
#
# except ZeroDivisionError as a:
#     print(a)
#     print("You can't divide by 0")
# except ValueError:
#     print("please provide only a number, sir!")
# except Exception:
#     print("something went wrong:( ")
# else:
#     print(result)
# finally:
#     print("Ok, Good bye sir!")



#
# import os
# path = "C:\\Users\\Kandarp Sharma\\Desktop\\Python\\Hello Moto"
# if os.path.exists(path):
#     print("That location exists")
#     if os.path.isfile(path):
#         print("That is a file! ")
#     if os.path.isdir(path):
#         print("That is a folder !")
# else:
#     print("That location doesn't exist")


# modules  = a file containing python code. May contain functions, classes, etc.
#           used with modular programming, which is to separate a program into parts



import sample


