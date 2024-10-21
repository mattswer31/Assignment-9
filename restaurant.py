restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu.update({"Beverages" : {}})
restaurant_menu["Beverages"].update({"Wine" : 9.50, "Sprite" : 2.50})
restaurant_menu.update({"Main Course" : {"Steak" : 17.99}})
restaurant_menu["Starters"].pop("Bruschetta")

for category in restaurant_menu:
    current_category = restaurant_menu[category]
    print(f"{category}")
    for item in current_category:
        print(f"{item}: {current_category[item]:.2f}")