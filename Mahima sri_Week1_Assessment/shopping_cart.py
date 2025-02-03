def add_item(cart):
    item_name = input("Enter the item name: ")
    item_price = float(input("Enter the item price: "))
    cart[item_name] = item_price
    print(f"Added {item_name} with price {item_price} to the cart.")

def view_cart(cart):
    if not cart:
        print("Your shopping cart is empty.")
    else:
        print("Items in your cart:")
        for item, price in cart.items():
            print(f"{item}: ${price:.2f}")
    
def calculate_total(cart):
    total = sum(cart.values())
    print(f"Total price: ${total:.2f}")

def main():
    shopping_cart = {}
    while True:
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_item(shopping_cart)
        elif choice == '2':
            view_cart(shopping_cart)
        elif choice == '3':
            calculate_total(shopping_cart)
        elif choice == '4':
            print("Exiting the shopping cart. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

main()
