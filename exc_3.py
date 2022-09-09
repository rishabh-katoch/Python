# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
yr_left = 90 - age

days_left = yr_left*365
week_left = yr_left*52
month_left = yr_left*12 

print(f"You have {days_left} days, {week_left} weeks, and {month_left} months left.")