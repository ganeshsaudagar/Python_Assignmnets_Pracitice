import json

with open ('admin.json') as file:
    data=json.load(file)
    data1=data[0]

    Admin_user=input("ENTER THE USER NAME")
    Admin_password=input("ENTER THE PASSWORD")

    if data1["username"]==Admin_user and data1["password"]==Admin_password:
        print("........WELCOME..........")
    else:
        print("PLEASE ENTER THE  CORRECT CREDENTIALS")