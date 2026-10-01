Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

country1 = None
country2 = None

if city1 in Australia:
    country1 = "Australia"
elif city1 in UAE:
    country1 = "UAE"
elif city1 in India:
    country1 = "India"

if city2 in Australia:
    country2 = "Australia"
elif city2 in UAE:
    country2 = "UAE"
elif city2 in India:
    country2 = "India"

if country1 is None or country2 is None:
    print("One or both cities were not found.")
elif country1 == country2:
    print("Both cities are in", country1)
else:
    print("They don't belong to the same country")
