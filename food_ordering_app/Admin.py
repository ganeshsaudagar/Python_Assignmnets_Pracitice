# Admin Module
admin_info={"Ganesh":"saudagar@22"}
# stock in Restaurent
menu_list={1:{'foodId':1,'Name':'Burger','Quantity':20,'Price':30,'Discount':5,'Stock':20},
           2:{'foodId':2,'Name':'Pizza','Quantity':15,'Price':100,'Discount':7,'Stock':15},
           3:{'foodId':3,'Name':'Cake','Quantity':8,'Price':200,'Discount':0,'Stock':8},
           }
# automatic Generated
food_id=3
def add_food_item():
    global food_id
    food_id+=1
    item_name=input("Enter food item Name ")
    item_quantity = int(input("Enter food item Quantity "))
    item_price = int(input("Enter food item Price "))
    item_discount = int(input("Enter food item Discount "))
    item_stock = int(input("Enter food item Stock "))

    # Check Whether id is present or not :
    if food_id in menu_list.keys():
        print("You Can't Add New Food Item!!!  Because Id is Present Already ")
    else :
        menu_list[food_id]={'foodId':food_id,
                            'Name':item_name,
                            'Quantity':item_quantity,
                            'Price':item_price,
                            'Discount':item_discount,
                            'Stock':item_stock
                            }
        print("Food Item is Successfully Added.......")

def edit_food_item():
    """First check id then You can edit """
    item_id = int(input("Enter food item id "))
    if item_id in menu_list.keys():
        print("Id  is Correct You can Edit !!!!")
        item_name = input("Enter food item Name ")
        item_quantity = int(input("Enter food item Quantity "))
        item_price = int(input("Enter food item Price "))
        item_discount = int(input("Enter food item Discount "))
        item_stock = int(input("Enter food item Stock "))
        # Update the Menu 
        menu_list[item_id]['Name']=item_name
        menu_list[item_id]['Quantity']=item_quantity
        menu_list[item_id]['Price'] = item_price
        menu_list[item_id]['Discount'] = item_discount
        menu_list[item_id]['Stock'] = item_stock
        print(f"{item_id}  is Updated Successfully.......!")
    
    else :
        print(f"{item_id}  is Not Present Inside the Menu List.......")
        

def show_menu_item():
    i=0
    for values in menu_list.values():
        i+=1
        print(i, values)

def removing_food_item():
    """Check Whether id id here or not """
    item_id = int(input("Enter food item id "))
    if item_id in menu_list.keys():
        del  menu_list[item_id]
        print(f"{item_id} is Deleted Successfully..!!!")
    else :
        print(f"{item_id} is Note Here in Menu List.......")
