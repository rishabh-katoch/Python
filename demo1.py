age = input("Enter age:")
age = int(age)
if age > 21:
    print("You are eligible for beer")
else:
    print("You are underage")

# for loop
food = ['fish', 'chapati', 'burger', 'chinese', 'continental']

for f in food:
    print("I love", f, " which has ", len(f) , " characters")