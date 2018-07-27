
# Letter Grade Bot

pointspossible = 100
score = 89.9
studentname = "Oleg"
grade = ""
percentage = (score / pointspossible) * 100
if 90 <= percentage <= 100:
	grade = "A"
elif 80 <= percentage < 90:
	grade = "B"
elif 70 <= percentage < 80:
	grade = "C"
elif 60 <= percentage < 70:
	grade = "D"
else:
	grade = "F"


print(studentname, grade)