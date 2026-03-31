# import math
#
# from babel.localedata import Alias
# from setuptools.command.alias import alias
#
# x = math.sqrt(25)
# print(x)
#
# print(math.floor(3.5))
#
# #import math as m (Alias)

marks = 75
if marks>80:
    print("You got A+ grade")
elif marks>70 and marks<80:
    print("you got B+ grade")
elif marks>50 and marks<70:
    print("congratulations! you are pass")
else:
    print("you are fail")

print("\n")
StudentName = ["Sheraz", "Azhar" , "Hameed", "Safeer"]

for i in range(len(StudentName)):
    print("Students Name: ",StudentName[i])


# for i in range(len(StudentName)):
#     #we use end=" " for ending space/not sapace
#     print("Students Name: ",StudentName[i] , end=" ")

thisdict = {
    "name" : "Sheraz",
    "Cast" : "Arisar",
    "age" : 21,
    "Qualification" : "Bachelor's"
}

print(thisdict)

# array