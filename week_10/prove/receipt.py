# Lucilene DeWeese
# Purpose: Read products.csv into a dictionary, process a customer's order from request.csv,
# print a formatted receipt with error handling, early bird discount, and coupon feature.

# Import the datetime class from the datetime module to work with dates and times
from datetime import datetime
# Import the random module to randomly select a product for the coupon feature
import random


# Step 1: Function to read products.csv into a compound dictionary
def read_products(filename):
    """
    Read the contents of products.csv into a compound dictionary.
    
    Parameters
        filename: the name of the CSV file to read
    Return: a dictionary with product number as keys and
            [product number, name, price] as values
    """
    products_dict = {}  # create empty dictionary

    with open(filename, "rt") as products_file:  # open file for reading
        next(products_file)  # skip header line
        for line in products_file:
            clean_line = line.strip()
            parts = clean_line.split(",")
            product_number = parts[0]
            products_dict[product_number] = parts

    return products_dict

# Step 2: Function to process a customer's order
def process_request(filename, products_dict):
    """
    Read request.csv, print items ordered, and calculate totals.
    Handles KeyError and FileNotFoundError.
    """
    try:
        print("Inkom Emporium\n")  # Store name

        subtotal = 0.0
        total_items = 0
        purchased_products = []

        with open(filename, "rt") as request_file:
            next(request_file)  # skip header line
            for line in request_file:
                clean_line = line.strip()
                prod_num, quantity = clean_line.split(",")
                quantity = int(quantity)

                try:
                    # Lookup product info (may raise KeyError)
                    product_info = products_dict[prod_num]
                    name = product_info[1]
                    price = float(product_info[2])
                    line_total = price * quantity

                    # Print item line in receipt format
                    print(f"{name}: {quantity} @ {price:.2f}")

                    subtotal += line_total
                    total_items += quantity
                    purchased_products.append(name)

                except KeyError as key_err:
                    print(f"\nError: unknown product ID in the request.csv file")
                    print(key_err)

        # Early bird discount (before 11 AM)
        current_time = datetime.now()
        discount = 0.0
        if current_time.hour < 11:
            discount = 0.10  # 10%
            print("\nEarly Bird Discount Applied: 10% off subtotal")
            subtotal *= (1 - discount)

        # Compute sales tax and total
        tax_rate = 0.06
        sales_tax = round(subtotal * tax_rate, 2)
        total = round(subtotal + sales_tax, 2)

        print(f"\nNumber of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}\n")

        print("Thank you for shopping at the Inkom Emporium.")

        # Print current date and time formatted like sample output
        print(current_time.strftime("%a %b %d %H:%M:%S %Y"))

        # Coupon for a purchased item
        if purchased_products:
            coupon_product = random.choice(purchased_products)
            print(f"\nCongratulations! You get a coupon for 10% off your next {coupon_product} purchase!")

    except FileNotFoundError as fnf_err:
        print("\nError: missing file")
        print(fnf_err)

# Step 3: Main function
def main():
    try:
        products_dict = read_products("products.csv")
        process_request("request.csv", products_dict)
    except FileNotFoundError as fnf_err:
        print("\nError: missing file")
        print(fnf_err)

# Step 4: Execute main if run directly
if __name__ == "__main__":
    main()
