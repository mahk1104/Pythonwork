# Prices
phone_prices = {"basic": 300, "standard": 500, "superior": 1000}
setup_options = {"a": 50, "b": 100}
setup_names = {"a": "Standard Setup", "b": "Premium Setup"}

from datetime import datetime

# Function to calculate total cost
def calculate_total_cost(quantity, phone_type, setup_option):
    phone_cost = phone_prices[phone_type] * quantity
    setup_cost = setup_options[setup_option] * quantity
    total_cost = phone_cost + setup_cost
    vat = total_cost * 0.2
    total_with_vat = total_cost + vat
    return phone_cost, setup_cost, total_cost, vat, total_with_vat

# Get current date and time 
current_time = datetime.now().strftime("%A, %d %B %Y at %H:%M:%S")

# Get customer details
customer_name = input("Enter customer name: ")
company_name = input("Enter company name: ")
contact_number = input("Enter contact number: ")

# Get quantity
while True:
    try:
        quantity = int(input("Enter quantity of smartphones (must be multiple of 5, between 5 and 100): "))
        if quantity % 5 == 0 and 5 <= quantity <= 100:
            break
        else:
            print("Invalid input. Quantity must be between 5 and 100 and a multiple of 5.")
    except ValueError:
        print("Please enter a valid number.")

# Get phone type
while True:
    phone_type = input("Enter smartphone type (basic/standard/superior): ").strip().lower()
    if phone_type in phone_prices:
        break
    else:
        print("Invalid phone type. Please choose from basic, standard, or superior.")

# Get setup option
while True:
    setup_option = input("Enter setup option (A/B): ").strip().lower()
    if setup_option in setup_options:
        break
    else:
        print("Invalid setup option. Please enter A or B.")

# Calculate costs
phone_cost, setup_cost, total_cost, vat, total_with_vat = calculate_total_cost(quantity, phone_type, setup_option)

# Print summary
summary = f"""
--- Quotation ---

Date and Time: {current_time}

Customer Details:
Name: {customer_name}
Company: {company_name}
Contact Number: {contact_number}

Smartphones:
Quantity: {quantity}
Type: {phone_type.capitalize()}
Phone cost: £{phone_cost:,.2f}

Setup Option:
Option: {setup_option.upper()} ({setup_names[setup_option]})
Total setup cost: £{setup_cost:,.2f}

Cost Summary:
Total cost (excl. VAT): £{total_cost:,.2f}
VAT (20%): £{vat:,.2f}
Total cost (incl. VAT): £{total_with_vat:,.2f}
"""

print(summary)

# Save to file
with open("quotation.txt", "w") as file:
    file.write(summary)

print("Quotation saved to 'quotation.txt'")
