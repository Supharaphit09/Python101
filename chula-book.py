students = {
    "Kate": 3.25,
    "Jib": 3.66,
    "Niky": 3.5,
    "Kato": 4.0,
    "Eve": 3.8
}

good_students = [name for name, grade in students.items() if grade > 3.5]

sorted_grades = sorted(students.items(), key=lambda x: x[1])


print("Student have a GPA more than 3.5:")
for name in good_students:
    print("- " + name)

print("GPA ascending:")
for name, grade in sorted_grades:
    print("- {}: {}".format(name, grade))