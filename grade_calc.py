#ex3, study drills #3
print "Welcome to the Magnificent Grade Calculator!"
print "----- This is a non-input version, so to change values, edit this file -----"

total_points = 1000.0
#homework grades
hw1 = 50.0
hw2 = 28.0
hw3 = 15.0
hw4 = 89.0

#midterm grades
mid1 = 78.0
mid2 = 92.0

#grade on final exam
final = 135.0

final_grade = ((hw1 + hw2 + hw3 + hw4 + mid1 + mid2 + final) / total_points) * 100.0

print "Your final grade average is: ", final_grade