resources = {"water": 300, "milk": 300, "coffee": 50, "money": 2}
menu = {
    "espresso": 
        {"ingredients": 
            {"water": 50, "coffee": 18}, 
         "cost": 1.5},
    "latte": 
        {"ingredients": 
            {"water": 200, "milk": 150, "coffee": 24}, 
         "cost": 2.5},
    "cappuccino": 
        {"ingredients": 
            {"water": 250, "milk": 100, "coffee": 24},
         "cost": 3.0,
    },
}

def resource_check(type_of_drink,money):
    #Ingredient check
    shortage = 0
    for resource in menu[type_of_drink]["ingredients"]:
        if menu[type_of_drink]["ingredients"][resource]>resources[resource]:
            print(f"Short on {resource}")
            shortage+=1
        
    #Cost check
    if money<menu[type_of_drink]["cost"]:
        print(f"{type_of_drink} costs ${menu[type_of_drink]['cost']}, you are short by {menu[type_of_drink]['cost']-money}")
        shortage+=1
        
    elif menu[type_of_drink]["cost"]-money>resources["money"]:
        print(f"Do not have enough change money, at present have {resources['cost']}")
        shortage+=1
    return shortage

def resource_update(type_of_drink,money):
    #Ingredients update
    for resource in menu[type_of_drink]["ingredients"]:
        resources[resource] = resources[resource]-menu[type_of_drink]["ingredients"][resource]
        
    #Cost update
    resources["money"] = resources["money"]-change+money
        
        
while True:
        
    option = input("What would you like? (espresso/latte/cappuccino)\n")
    if option not in ["espresso","latte","cappuccino","report","off"]:
        print("Entered incorrect value\n")
        continue
    
    if option.lower() == "report":
        print(f"Water: {resources['water']}ml\n")
        print(f"Milk: {resources['milk']}ml\n")
        print(f"Coffee: {resources['coffee']}g\n")
        print(f"Money: ${resources['money']}\n")
        continue        
    elif option.lower() == "off":
        print("Switching machine off\n")
        break
    
    try:        
        money = float(input(f"Please insert ${menu[option]['cost']}: "))
    except Exception as e:
        print("Entered incorrect value, please enter numeric value")
        continue
        
        
    if resource_check(option, money)>0:
        break
    
    if money>menu[option]["cost"]:
        change = money-menu[option]['cost']
        print(f"Here is your change: {change}")   
    
    print("Enjoy your drink!\n")
    
    resource_update(option,money)