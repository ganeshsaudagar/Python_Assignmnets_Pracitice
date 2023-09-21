import json
import random

with open("admin_data.json") as file:                         
    data=json.load(file)
    data1=data[0]
    Admin_user=input("ENTER ADMIN USERNAME:")
    Admin_password=input("ENTER ADMIN PASSWORD:")

if data1["username"]==Admin_user and data1["password"]==Admin_password:
    print("WELCOME ADMIN",Admin_user.upper())
    
else:
    print("Please ENTER CORRECT CREDENTIALS")

class Item_Details:
    def __init__(self,foodid,name,qty,price,discount,stock):
        self.foodid=random(100,999)
        self.name=name
        self.qty=qty
        self.price=price
        self.discount=discount
        self.stock=stock

class Food_Items:
    def __init__(self):
        self.food_items={}
    def add_food_items(self):
        name=input('enter name')
        qty=input("enter qty")
        price=input("enter price")
        discount=input("enter discount")
        stock=input("enter stock")

        obj=Food_Items(name,qty,price,discount,stock)
        obj.food_id=len(self.food_items+1)
        self.add_food_items.append(obj)
        print(self.food_items)
        print("food items added successfully")
Food_Items()