# day 1 
# Write a program in main.py that prints the same notes from the previous lesson using what you have learnt about the Python print function.
# Example Output After you have written your code, you should run your program and it should print the following:
# Example Output 

print("Day 1 - Python Print Function \n The function is declared like this: \n print('what to print')")

# Look at the code in the code editor on the right. There are errors in all of the lines of code. Fix the code so that it runs without errors.

#Fix the code below 👇

#print(Day 1 - String Manipulation")
#print("String Concatenation is done with the "+" sign.")
#  print('e.g. print("Hello " + "world")')
#print(("New lines can be created with a backslash and n.")

#fixed Code      
print("Day 1 - String Manipulation")
print('''String Concatenation is done with the "+" sign.''')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# program to find length of name
a = input("what is your name ? : \n")
print(len(a))

# Write a program that switches the values stored in the variables a and b.

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
c = a 
a = b
b = c 

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
