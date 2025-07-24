import datetime
import json
import os

ORDERS_FILE = "past_orders.json"
STAFF_PASSWORD = "admin123"

def load_past_orders():
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as file:
            return json.load(file)
    return []

def save_orders(orders):
    with open(ORDERS_FILE, "w") as file:
        json.dump(orders, file, indent=4)

def save_order(order):
    past_orders = load_past_orders()
    past_orders.append(order)
    save_orders(past_orders)

def delete_all_orders():
    save_orders([])

order_date = datetime.datetime.now().strftime("%d-%m-%y")
order_time = datetime.datetime.now().strftime("%H-%M-%S")

first_name = input("Please enter your first name: ").strip().title()
last_name = input("Please enter your last name: ").strip().title()

while True:
    table_number = input("Please enter your table number: ").strip()
    if table_number.isdigit():
        break
    print("Invalid table number! Please enter a number.")

print("\nWelcome to Byte and Brew Knightsbridge Cafe!!")

total_price = 0.0
items_ordered = {}

menu_items = {
    'food': {
        'wagyu beef steak': 120.00, 'truffle pasta': 150.00, 'foie gras terrine': 180.00,
        'lobster bisque': 130.00, 'caviar blinis': 200.00, 'gold leaf cheesecake': 250.00,
        'saffron risotto': 140.00, 'black truffle pizza': 220.00, 'foie gras burger': 190.00,
        'king crab salad': 160.00, 'duck confit': 170.00, 'venison loin': 180.00,
        'roasted quail': 150.00, 'sea bass en papillote': 140.00, 'foie gras ravioli': 200.00,
        'truffle scrambled eggs': 180.00, 'lobster thermidor': 240.00, 'black cod miso': 210.00,
        'beef wellington': 230.00, 'caviar and blinis': 220.00, 'oysters on ice': 160.00,
        'sous vide lamb': 180.00, 'king prawn cocktail': 150.00, 'seafood platter': 270.00,
        'chocolate souffle': 140.00, 'golden apple tart': 160.00, 'macaron assortment': 120.00,
        'cheese board deluxe': 190.00, 'lobster roll': 200.00, 'black truffle fries': 130.00,
        'scallops with caviar': 210.00, 'wild mushroom tart': 150.00, 'duck breast': 180.00,
        'grilled asparagus': 140.00, 'white truffle risotto': 220.00, 'braised short rib': 200.00,
        'lobster mac and cheese': 190.00, 'bluefin tuna tartare': 220.00, 'premium sushi platter': 300.00
    },
    'drinks': {
        'grand cru champagne': 250.00, 'aged scotch whisky': 300.00, 'vintage port wine': 220.00,
        'rare cognac': 280.00, 'luxury coffee blend': 50.00, 'single origin espresso': 40.00,
        'imported green tea': 30.00, 'handcrafted mojito': 75.00, 'classic martini': 80.00,
        'premium gin tonic': 70.00, 'aged rum': 90.00, 'organic matcha latte': 65.00,
        'caviar bloody mary': 150.00, 'gold leaf cappuccino': 120.00, 'iced saffron tea': 60.00,
        'luxury hot chocolate': 55.00, 'vintage red wine': 180.00, 'rare sake': 140.00,
        'artisan lemonade': 35.00, 'exotic fruit punch': 40.00, 'champagne cocktail': 130.00,
        'truffle infused cocktail': 160.00, 'blackberry brandy': 110.00, 'premium iced coffee': 50.00,
        'sparkling elderflower': 40.00, 'classic negroni': 75.00, 'aged tequila': 90.00,
        'golden turmeric latte': 45.00, 'french press coffee': 60.00, 'luxury chai latte': 55.00,
        'berry sangria': 70.00, 'handcrafted mojito': 75.00, 'artisan ginger beer': 40.00,
        'rare white rum': 85.00, 'aged bourbon': 120.00, 'exotic mango lassi': 55.00,
        'premium herbal tea': 35.00, 'luxury espresso martini': 140.00, 'champagne punch': 150.00
    },
    'desserts': {
        'gold leaf chocolate mousse': 180.00,
        'saffron panna cotta': 170.00,
        'black truffle ice cream': 160.00,
        'caviar and caramel tart': 210.00,
        'diamond dusted macarons': 200.00,
        'white chocolate and raspberry souffle': 190.00,
        'golden honey baklava': 150.00,
        'lavender crème brûlée': 140.00,
        'vanilla bean panna cotta': 130.00,
        'chocolate lava cake with gold flakes': 220.00,
        'passion fruit tartlet': 130.00,
        'rose petal cheesecake': 160.00,
        'black sesame parfait': 140.00,
        'rich tiramisu with aged espresso': 180.00,
        'caramelized fig tart': 150.00,
        'blood orange sorbet': 120.00,
        'hazelnut praline mille-feuille': 170.00,
        'matcha green tea mousse': 140.00,
        'dark chocolate ganache tart': 160.00,
        'pistachio and rose water cake': 150.00,
        'bourbon vanilla panna cotta': 160.00,
        'white chocolate raspberry trifle': 170.00,
        'golden saffron rice pudding': 140.00,
        'chocolate and chili fondant': 180.00,
        'almond and pear tart': 150.00,
        'vanilla bean crème caramel': 130.00,
        'hazelnut dacquoise': 160.00,
        'fig and almond frangipane': 150.00,
        'gold leaf profiteroles': 210.00,
        'dark cherry clafoutis': 140.00,
        'coconut and lime panna cotta': 130.00,
        'spiced apple tarte tatin': 160.00,
        'lemon verbena mousse': 140.00,
        'white chocolate and passion fruit bombe': 190.00,
        'café au lait mousse': 170.00,
        'caramel pecan tart': 150.00,
        'black currant sorbet': 120.00,
        'chocolate peanut butter tart': 160.00,
        'vanilla bean soufflé': 180.00,
    }
}

book_list = {
    'The Alchemist': 120.00, 'A Song of Ice and Fire': 150.00, 'Moby Dick': 130.00, 'Treasure Island': 160.00,
    'The Great Gatsby': 190.00, '1984': 210.00, 'The Woman in the Window': 170.00, 'The Silent Patient': 260.00,
    'Pride and Prejudice': 110.00, 'The Hobbit': 140.00, "Salem's Lot": 130.00, 'The War Horse': 90.00,
    'The Dance of Dragons': 230.00
}

def display_menu():
    print("\n*** Menu ***")
    for category, items in menu_items.items():
        print(f"\n{category.capitalize()}:")
        for item, price in items.items():
            print(f"  - {item.title()} : £{price:.2f}")
    print("\n*** Book List ***")
    for book, price in book_list.items():
        print(f"  - {book} : £{price:.2f}")

view_menu = input("Would you like to see the menu? (yes/no): ").strip().lower()
if view_menu in ['yes', 'y']:
    display_menu()

def get_quantity():
    while True:
        quantity = input("How many would you like? ").strip()
        if quantity.isdigit() and int(quantity) > 0:
            return int(quantity)
        print("Invalid quantity. Please enter a positive number.")

def handle_order(category):
    global total_price
    while True:
        item = input(f"What {category} would you like to order? ").lower()
        if item in menu_items[category]:
            quantity = get_quantity()
            price = menu_items[category][item]
            items_ordered[item] = items_ordered.get(item, 0) + quantity
            item_total = price * quantity
            total_price += item_total
            print(f"Added {quantity} x {item.title()} : £{item_total:.2f} to your order. Total so far: £{total_price:.2f}")
        else:
            print(f"Sorry, we don't have {item}. Please choose from the menu.")
            continue
        if input("Would you like to order more? (yes/no): ").lower() not in ['yes', 'y']:
            break

def handle_book_order():
    global total_price
    while True:
        book = input("What book would you like to order? ").title()
        if book in book_list:
            quantity = get_quantity()
            price = book_list[book]
            items_ordered[book] = items_ordered.get(book, 0) + quantity
            item_total = price * quantity
            total_price += item_total
            print(f"Added {quantity} x {book} : £{item_total:.2f} to your order. Total so far: £{total_price:.2f}")
        else:
            print(f"Sorry, we don't have the book '{book}'. Please choose from the book list.")
            continue
        if input("Would you like to order more books? (yes/no): ").lower() not in ['yes', 'y']:
            break

while True:
    order_type = input("\nWhat would you like to order? (food, drink, dessert, book) or 'exit' to finish: ").lower()
    if order_type == 'exit':
        break
    elif order_type == 'food':
        handle_order('food')
    elif order_type == 'drink':
        handle_order('drinks')
    elif order_type == 'dessert':
        handle_order('desserts')
    elif order_type == 'book':
        handle_book_order()
    else:
        print("Invalid choice. Please select from food, drink, dessert, book, or exit.")

print("\n--- Order Summary ---")
print(f"Name: {first_name} {last_name}")
print(f"Table Number: {table_number}")
for item, qty in items_ordered.items():
    if item in menu_items['food']:
        price = menu_items['food'][item]
    elif item in menu_items['drinks']:
        price = menu_items['drinks'][item]
    elif item in menu_items['desserts']:
        price = menu_items['desserts'][item]
    else:
        price = book_list.get(item, 0)
    print(f"{qty} x {item.title()} @ £{price:.2f} each = £{qty * price:.2f}")

print(f"\nTotal Price: £{total_price:.2f}")

order_data = {
    "name": f"{first_name} {last_name}",
    "table_number": table_number,
    "items_ordered": items_ordered,
    "total_price": total_price,
    "date": order_date,
    "time": order_time
}

save_order(order_data)

print("\nThank you for ordering at Byte and Brew Knightsbridge Cafe!")

# Staff menu to delete all orders (optional)
staff_mode = input("\nAre you staff? Enter password to access staff menu or press Enter to exit: ").strip()
if staff_mode == STAFF_PASSWORD:
    if input("Delete all past orders? (yes/no): ").lower() in ['yes', 'y']:
        delete_all_orders()
        print("All past orders have been deleted.")
else:
    print("Goodbye!")
