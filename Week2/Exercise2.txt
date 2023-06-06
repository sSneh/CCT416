def main():
    toppings = {
    "Pepperoni": 2.50,
    "Mushrooms": 1.75,
    "Onions": 1.50,
    "Bell Peppers": 1.75,
    "Olives": 2.00,
    "Spinach": 1.50,
    "Tomatoes": 1.25,
    "Bacon": 2.25}

    base_price = 12.00
    selected_toppings = []

    print("Welcome to out Pizzeria! What would you like to order?")

    for topping, price in toppings.items():
        print(f"- {topping}: ${price:.2f}")

    while True:
        topping = input("Please select a topping, or enter 'done' when you are finished: ")
        if topping == 'done':
            break
        elif topping in toppings:
            selected_toppings.append(topping)
        else:
            print("Sorry, we don't have that topping. Please try again.")

    total_cost = base_price
    for topping in selected_toppings:
        total_cost += toppings[topping]
  
    print(f"The total cost of your pizza is ${total_cost:.2f}.")



main()