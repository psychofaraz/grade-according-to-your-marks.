marks = int(input("ENTER YOUR MARKS: \n"))

if marks>=90:
	grade = "A"
elif marks>=80:
	grade = "B"
elif marks>=70:
	grade = "C"
elif marks>=60:
	grade = "D"
elif marks>=50:
	grade = "E"
else:
	    grade = "F"

print("Your Grade Is " + grade)