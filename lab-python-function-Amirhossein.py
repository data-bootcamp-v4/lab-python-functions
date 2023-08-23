products = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = {}
customer_orders = set()
def initialize_inventory(products):
  for item in products:
    inventory[item]= int(input(f"How many {item}s are there in the inventory?"))
  return inventory

def get_customer_orders():

    continue_ordering = True
    while continue_ordering:
        customer_orders.add((input(f"what is your order? ")))
        next_order = input(f"Was that all?(yes/no)")
        if next_order == 'yes':
            continue_ordering = False
    return customer_orders

def calculate_order_statistics(inventory, customers_orders):
    total_products_ordered = len(customer_orders)
    total_productas = sum(inventory.values())
    percentage_of_products_ordered = round(total_products_ordered / total_productas , 2)
    order_status = (total_productas, percentage_of_products_ordered)
    return order_status


def update_inventory(invetory, customers_orders):
   for product in customer_orders:
      inventory[product] -= 1

   
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


# 10th Assignment
print("Updated inventory has:")
for product,quantity in inventory.items():
  print(f"{product}:{quantity}")

