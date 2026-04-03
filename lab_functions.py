# Lista de productos
products = ["t-shirt", "mug", "hat", "book", "keychain"]

def initialize_inventory(products):
    inventory = {}
    for product in products:
        quantity = int(input(f"Enter quantity for {product}: "))
        inventory[product] = quantity
    return inventory

def get_customer_orders():
    customer_orders = set()
    
    while True:
        product = input("Enter a product name (or type 'done' to finish): ")
        if product == "done":
            break
        customer_orders.add(product)
    
    return customer_orders

def update_inventory(customer_orders, inventory):
    for product in customer_orders:
        if product in inventory:
            inventory[product] -= 1
    return inventory

def calculate_order_statistics(customer_orders, products):
    total = len(customer_orders)
    percentage = (total / len(products)) * 100
    return total, percentage

def print_order_statistics(order_statistics):
    total, percentage = order_statistics
    print("\nOrder Statistics:")
    print(f"Total Products Ordered: {total}")
    print(f"Percentage: {percentage:.2f}%")

def print_updated_inventory(inventory):
    print("\nUpdated Inventory:")
    for product, quantity in inventory.items():
        print(f"{product}: {quantity}")

if __name__ == "__main__":
    inventory = initialize_inventory(products)
    customer_orders = get_customer_orders()
    inventory = update_inventory(customer_orders, inventory)
    stats = calculate_order_statistics(customer_orders, products)
    print_order_statistics(stats)
    print_updated_inventory(inventory)


