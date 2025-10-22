# Python boxes

# Ask the users for the numbers of manufectured items
total_items = int(input("Enter the number of manufactured items: "))

# Ask the user for the number of items that the user will pack per box
items_per_box= int(input("Enter the number of items per box: "))

# Calculate the number of boxes needed
num_boxes = (total_items + items_per_box - 1) // items_per_box

# Print the result
print("Number of boxes needed:", num_boxes)