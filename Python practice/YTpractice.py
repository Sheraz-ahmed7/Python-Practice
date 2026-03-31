#Variables:

name = "Sheraz"
age = 25
height = 6.1
is_student = True

print(f"my name is {name}")
print(f"my age is {age}")
print(f"my height is: {height}")
print(f"is I am a student? {is_student}\n")

if is_student:
    print("I am a student")
else:
    print("I am not a student")

print("\n")

#Types Casting:

gpa = 3.3

gpa = int(gpa)
print(f"GPA after TypesCasting is: {gpa}")

#age = float(age)
print(f"Age after type casting to float is: {age}")

age = str(age)
print(f"Age after type casting to String is: {age}")
print(type(age))

age += "1"
print(age)

age = int(age)
print(age)
print(type(age))

name = bool(name)
print(name)

#Input():

name = input("What is your name?: ")
#age = input("How old are You?: ")
age = int(input("How old are You?: "))

print(f"My name is: {name}")
print(f"I am {age} years old.")

#for changing value of integer first we have to convert it into integer:
#age = int(age)

#also we can convert at the time of input:
#age = int(input("How old are You?: "))

age +=3
print(f"My age after 3 year will be {age}.")
