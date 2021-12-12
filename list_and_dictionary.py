lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

## print the student's name

student = [lloyd["name"],alice["name"],tyler["name"]]

print(student)

## print the student's homework

student = [lloyd["homework"],alice["homework"],tyler["homework"]]

print(student)

## print the student's quizzes

student = [lloyd["quizzes"],alice["quizzes"],tyler["quizzes"]]

print(student)

## print the student's tests

student = [lloyd["tests"],alice["tests"],tyler["tests"]]

print(student)

###Define a function called average that has one argument, numbers.

def average(numbers):
    for item in numbers:
        total = float (sum(numbers))
        return total / len(numbers)


##Write a function called get_average that takes a student dictionary (like lloyd, alice, or tyler) as input and returns his/her weighted average.

def get_average(student):
        homework = average(student.get("homework"))
        quizzes = average(student.get("quizzes"))
        tests = average(student.get("tests"))

        homework = homework * 0.1
        quizzes = quizzes * 0.3
        tests = tests * 0.6
        return homework + quizzes + tests
  
  
### Define a new function called get_letter_grade that has one argument called score. Expect score to be a number.

def get_letter_grade(score):
	if score >= 90:return "A"
    	
	elif score >= 80:return "B"
   		
	elif score >= 70:return "C"
    	
	elif score >= 60:return "D"
    	
	else:return "F"

###Define a function called `get_class_average` that has one argument, students. You can expect students to be a list containing your three students.

result=[]

def get_class_average(student):
  result.append(get_average(student))
  return result

###Finally, print out the result of calling get_class_averagewith your students list. Your students should be [lloyd, alice, tyler].

get_class_average(lloyd)
get_class_average(alice)
get_class_average(tyler)

print(result)

###Then, print the result of get_letter_grade for the class's average.

result_by_letter=[]
def get_class_average_by_letter(student):
  result_by_letter.append(get_letter_grade(get_average(student)))
  return result

get_class_average_by_letter(lloyd)
get_class_average_by_letter(alice)
get_class_average_by_letter(tyler)

print(result_by_letter)
