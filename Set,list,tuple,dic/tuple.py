#an ordered, immutable collection of items
#cannot change it after creation.

t = (1, 2, 3)

#creating tuples:
t1 = (1, 2, 3)
t2 = 1, 2, 3        # parentheses optional
t3 = (5,)

#Accessing Elements:
t = (10, 20, 30)
print(t[1])    # 20
print(t[-1])   # 30


#slicing:

print(t[0:2])  # (10, 20)


#replace:
t = (99,) + t[1:]