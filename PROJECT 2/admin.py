import random

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(1000, 9999)
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, entered_username, entered_password):
        return self.username == entered_username and self.password == entered_password

class Restaurant:
    def __init__(self):
        self.food_items = []
        self.admin = Admin("admin", "password")

    def add_food_item(self, food_id, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = food_id  # Assign the provided FoodID
        self.food_items.append(food_item)
        print("Food item added successfully!")

    def edit_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                print(f"Editing Food Item with FoodID: {food_id}")
                food_item.name = input("Enter new name: ")
                food_item.quantity = input("Enter new quantity (e.g., 100ml, 250gm, 4 pieces): ")
                food_item.price = float(input("Enter new price: "))
                food_item.discount = float(input("Enter new discount: "))
                food_item.stock = int(input("Enter new stock quantity: "))
                print("Food item edited successfully!")
                return
        print(f"Food item with FoodID {food_id} not found.")

    def display_menu(self):
        print("\n===== Menu =====")
        for food_item in self.food_items:
            print(f"FoodID: {food_item.food_id}")
            print(f"Name: {food_item.name}")
            print(f"Quantity: {food_item.quantity}")
            print(f"Price: ${food_item.price}")
            print(f"Discount: {food_item.discount}%")
            print(f"Stock: {food_item.stock} units")
            print()

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print(f"Food item with FoodID {food_id} removed successfully!")
                return
        print(f"Food item with FoodID {food_id} not found.")

restaurant = Restaurant()

while True:
    print("\n===== Food Ordering App =====")
    print("1. Admin Login")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        entered_username = input("Enter admin username: ")
        entered_password = input("Enter admin password: ")

        if restaurant.admin.login(entered_username, entered_password):
            while True:
                print("\n===== Admin Panel =====")
                print("1. Add New Food Item")
                print("2. Edit Food Item (by FoodID)")
                print("3. View Menu")
                print("4. Remove Food Item (by FoodID)")
                print("5. Logout")
                admin_choice = input("Enter your choice: ")

                if admin_choice == "1":
                    food_id = int(input("Enter FoodID: "))  
                    name = input("Enter food item name: ")
                    quantity = input("Enter quantity (e.g., 100ml, 250gm, 4 pieces): ")
                    price = float(input("Enter price: "))
                    discount = float(input("Enter discount: "))
                    stock = int(input("Enter stock quantity: "))
                    restaurant.add_food_item(food_id, name, quantity, price, discount, stock)
                elif admin_choice == "2":
                    food_id = int(input("Enter FoodID to edit: "))
                    restaurant.edit_food_item(food_id)
                elif admin_choice == "3":
                    restaurant.display_menu()
                elif admin_choice == "4":
                    food_id = int(input("Enter FoodID to remove: "))
                    restaurant.remove_food_item(food_id)
                elif admin_choice == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")
        else:
            print("Invalid admin credentials. Access denied.")
    elif choice == "2":
        print("Thank you for using the Food Ordering App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")