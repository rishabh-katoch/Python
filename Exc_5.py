# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1+name2
name = name.lower()

tr = name.count('t') +  name.count('r')+ name.count('u')+ name.count('e')

lv = name.count('l') +  name.count('o')+ name.count('v')+ name.count('e')

fin_score = int(str(tr) + str(lv)) 

if fin_score < 10 or fin_score > 90:
    print(f"Your score is {fin_score}, you go together like coke and mentos.")
elif fin_score >= 40 and fin_score <= 50:
    print(f"Your score is {fin_score}, you are alright together.")
else:
    print(f"Your score is {fin_score}.")