""" application provides user interaction to browse a grocery store's inventory, add items to a cart, view the cart, and proceed to checkout.

Key Features:

- A list of grocery items with names and prices
- Option to add items to the cart with customizable quantities
- Cart viewing, showing the selected items and their total cost
- A checkout system that clears the cart after completing the order

This beginner-friendly project demonstrates core programming concepts such as classes, methods, loops, and user input handling, making it an ideal Python project for anyone looking to improve their skills.
We explain each step of the process in detail, helping you to follow along and understand how to implement these features."""







class GroceryItem :
    def __init__(self,name,price):
        self.name=name
        self.price=price


class Grocerystore:
    def __init__(self):
        self.inventory=[
            GroceryItem("Bread",60),
            GroceryItem("Milk",80),
            GroceryItem("Butter",45),
            GroceryItem("Banana",70),
            GroceryItem("Bathroom Cleaner",150),
            GroceryItem("Sink Wiper",85),
            GroceryItem("Chips",20)
        ]
        self.cart=[]


    def display_item(self):
        print("\n Available Items:")
        for index, item in enumerate(self.inventory):
            print(f"{index + 1}.{item.name} - Rps{item.price: .2f}")

    def add_to_cart(self,item_number,quantity):
            if 0<item_number<len(self.inventory):
                item=self.inventory[item_number-1]
                self.cart.append((item,quantity))
            print(f"{item.name}x{quantity} added to your cart")


    def view_cart(self):
        if not self.cart:
            print("\n Your cart is empty")

        else:
            print("your cart:")
            total_cost=0
            for item,quantity in self.cart:
                cost=item.price*quantity
                print(f"{item.name}x{quantity} -Rps{cost}")
                total_cost+=cost
            print(f"Total bill is :{total_cost}")

    def checkout(self):
        if not self.cart:
            print("Your cart is empty.Add items before checkout")

        else:
            self.view_cart()
            print("Your payment is being processed")
            self.cart=[]



def main():
    store=Grocerystore()
    while True:
        print("\n 1.View Items ")
        print("\n 2.Add to cart")
        print("\n 3.View cart")
        print("\n 4.Checkout")
        print("\n 5. Exit")

        choice = int(input("Enter you choice from 1-5"))
        if choice == 1:
            store.display_item()
        elif choice == 2:
            store.display_item()
            item_number = int(input("\n Enter item number to add to cart:"))
            quantity = int(input("\n Enter quantity: "))
            store.add_to_cart(item_number, quantity)

        elif choice == 3:
            store.view_cart()

        elif choice == 4:
            store.checkout()

        elif choice == 5:
            print("\n Thankyou for using Grocery App :) ")
            break

    else:
        print("Invalid choice, please try again")

main()

