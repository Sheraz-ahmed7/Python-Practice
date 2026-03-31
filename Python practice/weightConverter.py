#Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    print("Your weight is: ", weight, "pounds")
elif unit == "L":
    weight = weight / 2.205
    print("Your weight is: ", weight, "Kg")
else:
    print(unit, " Unit is invelid")

