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
        print("invalid input, no tip charged.")
    return total


print("welcome to the tip calculator!")
items = int(input("how many items did you purchase? "))  # asks user how many items

foodItem = []  # initialize empty lists
cost = []
totalCost = 0  # initialize total sum

for i in range(items):  # loops through all items
    food_name = input(f"what was the name of item {i+1}? ")
    item_cost = float(input(f"what was the cost of the {food_name}? "))
    foodItem.append(food_name)  #stores item name in the list
    cost.append(item_cost)  # stores item cost in the list
    totalCost += item_cost  #sums up the cost

# add tax to the total cost
totalCost += totalCost * 0.1

# ask for tip
tip_percentage = int(input("how much would you like to tip? 10%, 15%, 18%, or 20%? "))
total_cost = calculateTip(totalCost, tip_percentage)

# display the total cost
print(f"your total sum, including tax and tip, equals: ${total_cost:.2f}") #printf statement to ensure 2 decimal spaces (learned this from codeQuest projects)
