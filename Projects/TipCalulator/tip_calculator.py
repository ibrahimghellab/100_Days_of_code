print("Welcome to the tip calculator!")
total=float(input("What's the total bill? $"))
tips=int(input("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
print(f"Each person should pay: ${round(((total+(total*(tips/100)))/people),2):.2f}")