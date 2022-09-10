# comments and break

number = int(input("Enter a number:"))
for n in range(101):
    if n is number:
        print(n, "is the number that was entered")
        break
    else:
        print(n)
'''
comments can be added by us3ing the three aposthrephe
'''

# write numbers less than the number entered divided by 100

num = int(input("Enter a number:"))
for x in range (num +1):
    if x%4 == 0:
        print(x)
        break
    else:
        print("No numbers found")

