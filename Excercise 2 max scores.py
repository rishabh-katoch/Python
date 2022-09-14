# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# print("Largest element is:", max(student_scores))
a = 0 
for num in range(0,len(student_scores)):
    if a < student_scores[num]:
        a = student_scores[num]
print(f"The highest score in the class is:{a}")


