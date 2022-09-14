#Write your code below this row 👇
a = int(input("Enter the even first number:"))
b = int(input("Enter the even second number:"))
total = 0
if a%2 or b%2 != 0:
    print("Enter even number")
elif a > b:
    print("Enter the first number smaller.")
else:
    for num in range (a,b+1,2):
        total = num + total
print(total)