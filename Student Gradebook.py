# subjects and grades from last semester
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# student subjects
subjects = ["physics", "calculus", "poetry", "history"]

# student grades
grades = [98, 97, 85, 88]

# adding subjects and grades as required
subjects.append("computer science")
grades.append(100)

# zip to combine subjects and grades
gradebook = list(zip(subjects, grades))

# adding subject and grade together as one entry
gradebook.append(("visual arts", 93))

# prints this semesters gradebook
print(list(gradebook))

# combining both semesters grades
full_gradebook = gradebook + last_semester_gradebook

# prints the whole gradebook over two semesters
print(full_gradebook)
