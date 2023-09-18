import random

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(1000, 9999)
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []
        
    def login(self, email, password):
        return self.email == email and self.password == password

    def place_order(self, restaurant):
        print("\n===== Available Food Items =====")
        for idx, food_item in enumerate(restaurant.food_items, start=1):
            print(f"{idx}. {food_item.name} ({food_item.quantity}) [INR {food_item.price}]")

        selections = input("Enter the numbers of the items you want to order (e.g., 2 3): ").split()
        selected_items = []

        for selection in selections:
            try:
                index = int(selection) - 1
                if 0 <= index < len(restaurant.food_items):
                    selected_items.append(restaurant.food_items[index])
            except ValueError:
                continue

        if not selected_items:
            print("No valid items selected.")
            return

        print("\n===== Selected Food Items =====")
        total_cost = 0
        for item in selected_items:
            print(f"{item.name} ({item.quantity}) [INR {item.price}]")
            total_cost += item.price

        confirm = input(f"\nTotal Cost: INR {total_cost}\nDo you want to place the order? (yes/no): ").strip().lower()
        if confirm == "yes":
            self.order_history.append({"items": selected_items, "total_cost": total_cost})
            print("Order placed successfully!")
        else:
            print("Your Order is not placed.")

    def view_order_history(self):
        print("\n===== Order History =====")
        for idx, order in enumerate(self.order_history, start=1):
            print(f"Order {idx}:")
            total_cost = order["total_cost"]
            print(f"Total Cost: INR {total_cost}")
            print("Ordered Items:")
            for item in order["items"]:
                print(f"{item.name} ({item.quantity}) [INR {item.price}]")
            print()

    def update_profile(self):
        print("\n===== Update Profile =====")
        self.full_name = input("Enter full name: ")
        self.phone_number = input("Enter phone number: ")
        self.email = input("Enter email: ")
        self.address = input("Enter address: ")
        self.password = input("Enter new password: ")
        print("Profile updated successfully!")

class Restaurant:
      def __init__(self):
        self.food_items = []
        self.admin = ("Admin", "Password")
        self.add_initial_food_items()
       
      def add_initial_food_items(self):
        self.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 10)
        self.add_food_item("Vegan Burger", "1 Piece", 320, 10, 20)
        self.add_food_item("Truffle Cake", "500gm", 900, 5, 15)
        self.add_food_item("Coffee","1 Piece",60, 10, 50 )

      def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("Food item added successfully!")

      def display_menu(self):
        print("\n===== Menu =====")
        for food_item in self.food_items:
            print(f"FoodID: {food_item.food_id}")
            print(f"Name: {food_item.name}")
            print(f"Quantity: {food_item.quantity}")
            print(f"Price: INR {food_item.price}")
            print(f"Discount: {food_item.discount}%")
            print(f"Stock: {food_item.stock} units")
            print()
            
restaurant = Restaurant()
users = []

while True:
    print("\n===== Food Ordering App =====")
    print("1. User Registration")
    print("2. User Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n===== User Registration =====")
        full_name = input("Enter full name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        password = input("Enter password: ")
        user = User(full_name, phone_number, email, address, password)
        users.append(user)
        print("User registration successful!")

    elif choice == "2":
        email = input("Enter email: ")
        password = input("Enter password: ")
        user = None
        for u in users:
            if u.login(email, password):
                user = u
                break
        if user:
            while True:
                print("\n===== User Panel =====")
                print("1. Place New Order")
                print("2. Order History")
                print("3. Update Profile")
                print("4. Logout")
                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    user.place_order(restaurant)
                elif user_choice == "2":
                    user.view_order_history()
                elif user_choice == "3":
                    user.update_profile()
                elif user_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid login credentials.")

    elif choice == "3":
        print("Thank you (HOLA) for using the Food Ordering App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

