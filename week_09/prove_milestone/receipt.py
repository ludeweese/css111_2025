#Lucilene DeWeese
# receipt.py
# Purpose: Read products.csv into a compound dictionary and process a customer's order from request.csv

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
        next(products_file)  # skip the header line
        for line in products_file:
            clean_line = line.strip()  # remove leading/trailing whitespace
            parts = clean_line.split(",")  # split CSV line into parts
            product_number = parts[0]  # first column is the key
            products_dict[product_number] = parts  # store entire row as value

    return products_dict

# Step 2: Function to read request.csv and process each row
def process_request(filename, products_dict):
    """
    Read the request.csv file and print the requested items.
    
    Parameters
        filename: the name of the request CSV file
        products_dict: dictionary containing all products
    """
    print("\nRequested Items")
    
    with open(filename, "rt") as request_file:  # open file for reading
        next(request_file)  # skip the header line
        for line in request_file:
            clean_line = line.strip()  # remove leading/trailing whitespace
            product_number, quantity = clean_line.split(",")  # split CSV line
            quantity = int(quantity)  # convert quantity to integer
            
            # look up product in products_dict
            product_info = products_dict.get(product_number)
            if product_info:
                name = product_info[1]  # product name
                price = product_info[2]  # product price
                print(f"{name}: {quantity} @ {price}")
            else:
                print(f"Product {product_number} not found in products catalog.")

# Step 3: Main function to call the other functions
def main():
    # Read products.csv into a dictionary
    products_dict = read_products("products.csv")
    
    # Print all products dictionary
    print("All Products")
    print(products_dict)
    
    # Process the customer order from request.csv
    process_request("request.csv", products_dict)

# Step 4: Call main function only if this file is run directly
if __name__ == "__main__":
    main()
