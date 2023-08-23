products = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = {}
customer_orders = set()
#def initialize_inventory(produ)



# 3rd Assignment
for item in products:
  inventory[item]= int(input(f"How many {item}s are there in the inventory?"))

# 5th Assignment
"""
for orders in range(3):
   customer_orders.add(input(f"what is the order #{orders+1}:"))
"""
continue_ordering = True
while continue_ordering:
   customer_orders.add((input(f"what is your order? ")))
   next_order = input(f"Was that all?(yes/no)")
   if next_order == 'no':
    continue_ordering = False

# 6th Assignment
print("Your orders are:")
for orders in customer_orders:
  print(orders)

# 7th Assignment
total_products_ordered = len(customer_orders)
total_productas = sum(inventory.values())
percentage_of_products_ordered = round(total_products_ordered / total_productas , 2)
order_status = (total_productas, percentage_of_products_ordered)

# 8th Assignment
print("Order Statistics:")
print(f"Total Products Ordered: {total_products_ordered}")
print(f"Percentage of Products Ordered: {percentage_of_products_ordered * 100}%")

# 9th Assignment
for product in customer_orders:
  inventory[product] -= 1

# 10th Assignment
print("Updated inventory has:")
for product,quantity in inventory.items():
  print(f"{product}:{quantity}")

