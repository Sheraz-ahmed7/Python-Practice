# arr = [10, 20, 30, 40]
#
# print(arr[0])   # 10
# print(arr[2])   # 30
# print(arr[-1])  # 40 (last element)
#
# print("Array elements: ")
# for i in range(len(arr)):
#     print(arr[i],end=" ")
# print()
#
# print("Direct access: ")
# for x in arr:
#     print(x)
#
#
# #modifying array:
# arr[1] = 99
# print(arr)   # [10, 99, 30, 40]
#
# #add elements:
# arr.append(50)
#
# #insert :
#
# arr.insert(2, 25)   # index 2 par 25 insert
#
# print(arr)
#
# #Add multiple elements
# arr.extend([60, 70])
# print(arr)
#
# #Removing Elements
# arr.remove(30)
# arr.pop()
# print(arr)
# arr.pop(1)
# print(arr)
# del arr[0]
# print(arr)


#Slicing
arr1 = [10, 20, 30, 40, 50]

print(arr1[1:4])   # [20, 30, 40]
print(arr1[:3])    # [10, 20, 30]
print(arr1[2:])    # [30, 40, 50]
print(arr1[::-1])  # reverse list

#Searching in Array:
if 30 in arr1:
    print("found")
print()

#Sorting and Reversing
arr1.sort()          # ascending
arr1.sort(reverse=True)
arr1.reverse()       # reverse order
print(arr1)

new_arr = sorted(arr1)
print("Sorted Array: ",new_arr)
