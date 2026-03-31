print("hi")

thislist = ["AI", "IS", "Probability and statistics", "Software Req", "Soft. Arch And design", "Assembply laguange"]
print(thislist)

print(len(thislist))

print(thislist[-1])
print(thislist[2:5])

print(thislist[2:])

print(thislist[:5])

if 'IS' in thislist:
    print("Yes, IS is in thislist")

print(thislist)
thislist.remove('IS')
print(thislist)

thislist.insert(5,'IS')
print(thislist)

teacherList = ["Khorsheed", "Irshad Nazeer", "Farhan Bhutto"]
print(teacherList)

thislist.extend(teacherList)
print(thislist)
#print(thislist.extend(teacherList))

print('\nClear')
teacherList.clear()
print(teacherList)


print('\nReverse')
thislist.reverse()
print(thislist)
