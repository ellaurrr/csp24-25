def calculateTip(total, tip_percentage):  # calculates the tip based on user input
    if tip_percentage == 10:
        total += total * 0.1
    elif tip_percentage == 15:
        total += total * 0.15
    elif tip_percentage == 18:
        total += total * 0.18
    elif tip_percentage == 20:
        total += total * 0.2
    else:
        print("Invalid input, no tip charged.")
    return total

def calculateSum(): #function to calculate sum
    total = 0
    for i in range(items):  # loops through all items
        food_name = input(f"What was the name of item {i + 1}? ")
        item_cost = float(input(f"What was the cost of the {food_name}? "))
        foodItem.append(food_name)  # stores item name in the list
        cost.append(item_cost)  # stores item cost in the list
    for i in range(items): #loops to add costs into a total sum
        total += cost[i]
    return total

print("Welcome to the tip calculator!")
items = int(input("How many items did you purchase? "))  # asks user how many items

foodItem = []  # initialize empty lists
cost = []
totalCost = 0  # initialize total sum

totalCost = calculateSum()

# add tax to the total cost
totalCost += totalCost * 0.1

# ask for tip
tip_percentage = int(input("How much would you like to tip? 10%, 15%, 18%, or 20%? "))
total_cost = calculateTip(totalCost, tip_percentage)

# display the total cost (learned printf statements from outside source)
print(f"Your total sum, including tax and tip, equals: ${total_cost:.2f}")
