# # Task 1:

studentsMarks = {
    "Sheraz" : 90,
    "Hameed" : 87,
    "Azhar" : 75,
    "Safeer" : 80,
    "Mohsin" : 93
}

print(studentsMarks)

total = 0
count = 0

for name in studentsMarks:
    mark = studentsMarks[name]
    if 0 <= mark <= 100:
        total += mark
        count += 1
    else:
        print("Invalid mark:", name, mark)

average = total / count
print(average)

top_mark = -1
top_student = ""

for name,mark in studentsMarks.items():
    if mark>=90:
        grade ="A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "F"

    print(name, ":", grade)

    if mark >top_mark:
        top_mark = mark
        top_student = name

print(f"\nTop Performer: {top_student} with {top_mark} marks")

#task 3:

import numpyPractice as np

sensor_readings = np.array([23.4, 105.1, -2.0, 24.5, 26.0, 23.9])
print("Sensor readings:", sensor_readings)

invalid_mask = (sensor_readings < 0) | (sensor_readings > 100)
print("Invalid readings mask:", invalid_mask)

invalid_readings = sensor_readings[invalid_mask]
print("Invalid readings:", invalid_readings)

valid_readings = sensor_readings[~invalid_mask]
avg_valid = np.mean(valid_readings)
print("Average of valid readings:", avg_valid)

sensor_readings[invalid_mask] = avg_valid
print("Cleaned readings:", sensor_readings)

corrupted_count = np.sum(invalid_mask)
print("Number of corrupted readings:", corrupted_count)



