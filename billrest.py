menu = { #dictionary named menu where keys are food items and values are its prices.
    "idly": 10,
    "dosa": 15,
    "vada": 12
}
def additeminmenu():
    global menu #the function will use the menu variable defined outside of the function's scope.
    while True: #This initiates an infinite loop that continues until explicitly break
        item_name = input("Enter food item: ")
        item_price = float(input("Enter price: Rs. "))
        menu[item_name] = item_price  #adds the new item and its price to the menu dictionary.
        choice = input("Want to add another item? (Y/N) ")
        if choice.upper() != 'Y':
            break

def printmenu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item} Rs. {price}")

def calculate_bill():
    global menu
    total_bill = 0
    ordered_items = []
    while True:
        item_name = input("Enter food item: ")
        if item_name not in menu:
            print("Item not found in menu!")
            continue
        quantity = int(input("Enter quantity: "))
        total_price = menu[item_name] * quantity
        total_bill += total_price
        ordered_items.append((item_name, quantity, total_price))
        choice = input("Want to add another item? (Y/N) ")
        if choice.upper() != 'Y':
            break

    print("Item   Qty   Price   Total")
    for item, qty, price in ordered_items:
        print(f"{item}   {qty}   {menu[item]} Rs. {price}")

    print(f"Total Bill is Rs. {total_bill}")

    apply_discount = input("Do you have a promo code? (Y/N) ")
    if apply_discount.upper() == 'Y':
        promo_code = input("Enter promo code: ")
        if promo_code.upper() == "SAYUR10":
            discount = 10
            total_bill -= discount
            print(f"Discount is Rs. {discount}")
            print(f"Total Bill after discount is Rs. {total_bill}")
        else:
            print("Invalid promo code!")
    else:
        print(f"Total Bill is Rs. {total_bill}")

while True:
    print("\nEnter an option...")
    print("1. Add an item to Menu")
    print("2. Menu")
    print("3. Order and Bill")
    print("4. End")

    option = int(input())

    if option == 1:
        additeminmenu()
    elif option == 2:
        printmenu()
    elif option == 3:
        calculate_bill()
    elif option == 4:
        break
    else:
        print("Invalid option!")
