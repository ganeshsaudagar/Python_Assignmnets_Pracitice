admin={"id":"ganesh","password":"Ganesh@123"}

item_list={}
food_id=0

def food_item_list():
    global food_id
    food_id+=1
    item_name=input("ENTER FOOD ITEM NAME:")
    item_qty=input("ENTER THE NUMBER OF QUANTITY:")
    item_price=input("ENTER THE PRICE")
    item_discount=input("ENTER THE DISCOUNT")
    item_stock=input("ENTER STOCK AVAILABLE")

    if food_id in item_list.keys():
        print("CANT ADD ITEM....FOOD ITEM IS EXIST.")
    else:
        for i in input():
             print('ADD ITEM LIST:')
             food_item_list()
             item_list[food_id]={{"food_id":food_id,
                             "name":item_name,
                             "qty":item_qty,
                             "price":item_price,
                              "discount":item_discount,
                              "stock":item_stock}}
             item_list.append(item_list)
             print("item added successfully")
food_item_list()
print(item_list)


"""
print('ADD ITEM LIST:')
food_item_list()
item_list[food_id]={{"food_id":food_id,
                    "name":item_name,
                    "qty":item_qty,
                    "price":item_price,
                    "discount":item_discount,
                    "stock":item_stock}}
item_list.append(item_list)
print("FOOD ITEM ADDED SUCEESSFULLY.....")
"""


   




