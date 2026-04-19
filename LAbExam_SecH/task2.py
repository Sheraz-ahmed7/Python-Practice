#Use Dictionaries and Boolean logic to process data.
#You have a dictionary representing a simple weather station: weather = {"Monday": 32, "Tuesday": 28, "Wednesday": 35, "Thursday": 25}.
#Write a for loop to iterate through the dictionary.
weather = {"Monday": 32, "Tuesday": 28, "Wednesday": 35, "Thursday": 25}
for day, temperature in weather.items():
    #Inside the loop, use an if-else statement to print "Heatwave Warning" if the temperature is 30 or above, and "Normal" otherwise.
    if temperature >= 30:
        print(f"{day}: Heatwave Warning")
    else:
        print(f"{day}: Normal")

#3.Find the maximum temperature in the dictionary and store it in a variable.
max_temperature = max(weather.values())
print(f"Maximum Temperature: {max_temperature}")
