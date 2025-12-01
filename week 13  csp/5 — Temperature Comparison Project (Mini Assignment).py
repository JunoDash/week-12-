# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:

tempature = int(input("What's today's tempature? "))

if tempature in range(-10, 51):
    print("It's cold.")
elif tempature in range(51, 80):
    print("It's warm.")
elif tempature in range(80, 111):
    print("It's hot.")
else:
    print("Extreme tempature warning!")
