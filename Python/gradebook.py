last_semester_gradebook = [["Politics", 80], ["Latin", 96], ["Dance", 97], ["Architecture", 65]]

#Your code below: 

#Subjects and grades
subjects = ["Physics", "Calculus", "Poetry", "History"]
grades = [98, 97, 85, 88]

#Empty grade book
gradebook = []

#Combine arrays
for x in range(len(subjects)):
    tmpArray = [subjects[x], grades[x]]
    gradebook.append(tmpArray)

#Add computer science grade
computerScienceGrade = ["Computer Science", 100]
gradebook.append(computerScienceGrade)

#Add visual arts grade
visualArtsGrade = ["Visual Arts", 93]
gradebook.append(visualArtsGrade)

#Add 5 marks to visual arts grade
gradebook[5][1] += 5

#Change poetry grade from numerical value to "Pass/Fail"
gradebook[2].remove(85)
gradebook[2].append("Pass")

#Combine gradebook and last_semester_gradebook into full_gradebook
full_gradebook = gradebook + last_semester_gradebook
print(full_gradebook)
