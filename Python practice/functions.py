name= "sheraz"
def greeting(name):
    print("welcome ",name)

result = greeting(name)
print(result)

# # with 3 parameters
def student(name , dep):
    print("Student name is: ",name)
    print("student department is: ",dep)

student("Sheraz", "SE")

# return in functions

def greeting(name):
    print("welcome ", name)
    return name

result = greeting("Sheraz")
print(result)