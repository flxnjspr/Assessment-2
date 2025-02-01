#VENDING MACHINE V5

# Creating a dictionary for the items
menu = {
    "C1": {"name": "Chips Ahoy", "price": 1.50, "stock": 5},
    "R1": {"name": "Reese's", "price": 1.25, "stock": 5},
    "N1": {"name": "Nutella Biscuits", "price": 0.75, "stock": 5},
    "K1": {"name": "Kit Kat", "price": 1.00, "stock": 5},
    "S1": {"name": "Snickers", "price": 1.50, "stock": 5},
    "M1": {"name": "M&M's", "price": 2.00, "stock": 5},
    "W1": {"name": "Water", "price": 1.00, "stock": 5},
    "L1": {"name": "Lay's", "price": 9.65, "stock": 5},
    "H1": {"name": "Hershey", "price": 1.50, "stock": 5},
    "P1": {"name": "Pringles", "price": 7.25, "stock": 5},
}

def showMenu():
    print("\n||=======================================================||")
    print("||          Welcome to Felix's Vending Machine!          ||")
    print("||=======================================================||")
    print("|| Code | Item                 | Price (AED) | Stock     ||")
    print("||======|======================|=============|===========||")
    for code, item in menu.items():
        print(f"|| {code:<4} | {item['name']:<20} | {item['price']:<11.2f} | {item['stock']:<9} ||")
    print("||=======================================================||")

def payment(total_price):
    total_inserted = 0
    while total_inserted < total_price:
        try:
            remaining = total_price - total_inserted
            print(f"\nThe total cost is AED {remaining:.2f}.")
            amount = float(input("Insert money (AED): "))
            if amount <= 0:
                print("Please insert a valid amount.")
            else:
                total_inserted += amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    return total_inserted

def calculateChange(change):
    denominations = [1.00, 0.25, 0.10, 0.05, 0.01]
    change_breakdown = {}
    for denom in denominations:
        count = int(change // denom)
        if count > 0:
            change_breakdown[denom] = count
            change -= count * denom
            change = round(change, 2)
    return change_breakdown

def addFreeDrink():
    drink_code = "W1"
    if menu[drink_code]["stock"] > 0:
        menu[drink_code]["stock"] -= 1
        print("\nCongratulations! You have earned a free drink (Bottled Water) because you purchased 3 items. It has been dispensed.")
    else:
        print("\nWe're sorry. You would have earned a free drink, but bottle water is out of stock.")

def main():
    total_spent = 0.0
    purchase_count = 0
    cart = []
    total_price = 0.0

    while True:
        showMenu()
        choice = input("\nEnter the code of the product you want to purchase: ").upper()

        if choice in menu:
            item = menu[choice]
            if item['stock'] > 0:
                print(f"\nYou have selected {item['name']} for AED {item['price']:.2f}.")
                cart.append((item['name'], item['price']))
                total_price += item['price']
                item['stock'] -= 1
                purchase_count += 1

                another = input("\nDo you want another product? (yes/no): ").strip().lower()
                if another != 'yes':
                    print("\nYour selected items:")
                    for item_name, price in cart:
                        print(f" - {item_name}: AED {price:.2f}")

                    print(f"\nThe total amount to pay is AED {total_price:.2f}.")
                    total_inserted = payment(total_price)
                    change = total_inserted - total_price

                    print(f"\nThank you for your purchases! Your change is AED {change:.2f}.")
                    change_breakdown = calculateChange(change)
                    if change_breakdown:
                        print("\nYour change breakdown:")
                        for denom, count in change_breakdown.items():
                            print(f"AED {denom:.2f}: {count} coins/bills")

                    print("\nItems dispensed:")
                    for item_name, _ in cart:
                        print(f" - {item_name}")


                    if purchase_count >= 3:
                        addFreeDrink()

                    print(f"\nThank you for using Felix's vending machine! You spent a total of AED {total_price:.2f}.")
                    break
                else:
                    print("Sorry, those are not in the options. Please enter yes or no")
            else:
                print(f"\nSorry, {item['name']} is out of stock.")
        else:
            print("\nInvalid product code. Please try again.")

if __name__ == "__main__":
    main()
