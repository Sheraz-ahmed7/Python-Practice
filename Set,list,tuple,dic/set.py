# s = {1, 2, 2, 3}
# print(s)   # {1, 2, 3}
#
#
# nums = [1, 2, 2, 3, 4, 4]
# unique_nums = set(nums)
# print(unique_nums)   # {1, 2, 3, 4}
#
# #Adding & Removing
# s.add(10)
# s.remove(2)      # error if not found
# s.discard(99)    # no error
#
# print(s)
#

#Set Operations

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # union → {1, 2, 3, 4, 5}
print(a & b)   # intersection → {3}
print(a - b)   # difference → {1, 2}
print(a ^ b)   # symmetric difference → {1, 2, 4, 5}


