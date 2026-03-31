#Task 1:

#1;
age = 20
height =5.9
name = "Sheraz Ahmed"
#2:

print("Age is: ",(age))
print("height is: ",height)
print("Name is: ", name)

#3:

age = age + 5
print("Age after 5 years is: ",(age))

height_cm = height * 100
print("Height in cm: ",height_cm)

#4:


#Task 2:

#1:
CityList = ["Hyderabad", "Sukkur", "Ghotki", "Khairpur", "Umarkot"]
countries = ("Pakistan", "India", "USA", "Germany", "Japan")
languages = {"Sindhi", "Urdu", "Bangali", "Hindhi", "sraiki"}

#2
CityList.insert(2,'Nawabshah')
print(CityList)

print(countries[3])

languages.add('English')
print(languages)

#3
CitySet = set(CityList)
languagesList = list(languages)

#task 3:

#1
StudentName = "Sheraz"
rollNo = 110
percentage = 97.5

#2

MarksList = [90, 60, 78, 83, 87]
MarksTuple = (90, 60, 78, 83, 87)
MarksSet = {90, 60, 78, 83, 87}

#3:
total = sum(MarksList)
average = total / len(MarksList)

if 85 in MarksTuple:
    print(85, "is present in the tuple")
else:
    print(85,"is not present in the tuple")

MarksSet.add(85)

#4:

print("Student Name: ",StudentName)
print("Student roll number: ",rollNo)
print("Student Percentage: ",percentage)

print("Mark List: ",MarksList)
print("Mark tuple: ",MarksTuple)
print("Mark set: ",MarksSet)

#5:
#A set may contain fewer elements than a list because:
#Sets store only unique elements duplicates are automatically removed.
#Lists can have duplicates all repeated items are kept.