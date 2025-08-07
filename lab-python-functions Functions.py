# Functions 

### Initialize Inventory
def initialize_inventory(products):
    inventory = {}
    for product in products:
        quantity = int(input(f"Enter initial quantity for {product}: "))
        inventory[product] = quantity
    return inventory

### 2. Get customer orders
def get_customer_orders():
    customer_orders = set()
    while True:
        product_name = input("Enter product name to order (or 'done' to finish): ").strip()
        if product_name.lower() == 'done':
            break
        customer_orders.add(product_name)
    return customer_orders

### 3. Update inventory
def update_inventory(customer_orders, inventory):
    for product in customer_orders:
        if product in inventory and inventory[product] > 0:
            inventory[product] -= 1
        elif product in inventory:
            print(f"⚠ {product} is out of stock!")
        else:
            print(f"⚠ {product} does not exist in inventory!")


### 4. Calculate order statistics
def calculate_order_statistics(customer_orders, products):
    total_products_ordered = len(customer_orders)
    unique_products_ordered = len(customer_orders.intersection(products))
    percentage_unique = (unique_products_ordered / len(products)) * 100 if products else 0
    return total_products_ordered, percentage_unique


# 5. Print order statistics
def print_order_statistics(order_statistics):
    total_products_ordered, percentage_unique = order_statistics
    print("\n📊 Order Statistics:")
    print(f"Total products ordered: {total_products_ordered}")
    print(f"Percentage of unique products ordered: {percentage_unique:.2f}%")


# 6. Print updated inventory
def print_updated_inventory(inventory):
    print("\n📦 Updated Inventory:")
    for product, quantity in inventory.items():
        print(f"{product}: {quantity}")
