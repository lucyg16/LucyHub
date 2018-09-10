
gradeInClass = float(raw_input("Enter the grade you have in the class: "))
gradeDesired = float(raw_input("Enter the grade you would like in the class: "))
percentFinal = float(raw_input("Enter the percent that the final is: "))

gradeNeeded = 100*(gradeDesired - gradeInClass*(100-percentFinal)/100) / percentFinal 

print("You need " + str(gradeNeeded) + "% on the final to get a " + str(gradeDesired))
print("Good luck!")