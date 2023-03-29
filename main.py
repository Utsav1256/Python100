#Variables
name ="Utsav"
print(name)
name = " Muskan"
print(name)

name = input("What is your name?")
length = len(name)
print(length)

# Write a program that switches the values stored in the variables a and b. 
# # Example Input
# a: 3
# b: 5
# # Example Output
# a: 5
# b: 3
a = input("a : ")
b = input("b : ")

temp = a
a = b
b = temp
print("a : " + a)
print("b : " + b)