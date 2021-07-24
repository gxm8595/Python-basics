# index operator [] = gives acceess to a sequence's elements(str,list,tuples)

# name = "Gaurav Sharma"
# if(name[0].islower()):
#     name = name.upper()
# f_name = name[0:6].upper()
# print(f_name)

# function = a block of code is executed only when if it is called:
#
# def GXM(name, fame):
#     print("Hello "+ name + ". \nYou are having a nice "+ fame )
#     print("You can learn from me")
# GXM("Guy", "Attitude")

# Return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the fuction's return value.

# def multiply(num1, num2):
#     return num1*num2

# Keyword Arguments =  argumments  proceded by an identifier when we pass them to a function.
#                      The order of the arguments doesn't matter, unlike positional arguments
#                      Python knows the names of the arguments that our functional receives

#
# def names(first,middle,last):
#     print("Hello "+ first + " " + middle + " "+ last)
# names(last = "Gaurav", middle = "Kumar" ,first=" Sharma")


# nesed function calls  =  function calls inside other function calls
#                          innermost function calls are resolved first
#                          returned value is ised as arguments for the next outer function

# num = input("Enter a positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)
#
# Insted of writing this much lengthy code we can write only this code
# print(round(abs(float(input("Enter a positive number: ")))))




  #              Python uses Rule = L(local)E(enclosing)G(global)B(built-in) or LEGB
# scope = The region that a variable is recorginised
#         A variable is only available from inside the region if it is created:
#         A global and locally scoped versions of a variable can be created


# name = "Gaurav Sharma"   #global scope(available inside and outside function)
# def display_name():
#     name = "Gaurav"  # local scope(available only inside this function)
#     print(name)
# display_name()
# print(name)





# *args = parameters that will arguments into a tuple
#         useful so that function can accept a varying amount of arguments

# def add(*name):
#     sum = 2
#     name = list(name)
#     name[1] = 10
#     for i in name:
#         sum+= i
#     return sum
#
# print(add(1,2))

