numbers = [1, 2, 3, 4]
# names = ["Ali", "Sara", "John"]
# mixed = [1, "hello", 3.5, True]
#
# print(numbers[0])
# print(names[1])

# nums = [1, 2, 3]
# nums[1] = 99
# print(nums)
#
# #oprations:
#
# #Add elements
# nums.append(4)        # add at end
# nums.insert(1, 50)
#
# print(nums)
#
# # Remove:
# nums.remove(99)   # removes value
# nums.pop()        # removes last
# nums.pop(0)  # removes by index
#
# print(nums)

#Slicing Lists:

nums = [10, 20, 30, 40, 50]
print(nums[1:4])   # [20, 30, 40]
print(nums[:3])    # [10, 20, 30]
print(nums[::2])   # [10, 30, 50]


# Nested Lists:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[1][2])   # 6
