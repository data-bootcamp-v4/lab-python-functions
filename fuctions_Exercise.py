# Product list
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
        product = input("Enter the name of a product to order: ").lower()
        customer_orders.add(product)

        another = input("Do you want to add another product? (yes/no): ").lower()
        if another != "yes":
            break

    return customer_orders


def update_inventory(customer_orders, inventory):
    for product in customer_orders:
        if product in inventory and inventory[product] > 0:
            inventory[product] -= 1


def calculate_order_statistics(customer_orders, products):
    total_products_ordered = len(customer_orders)
    percentage_unique = (total_products_ordered / len(products)) * 100

    order_statistics = (total_products_ordered, percentage_unique)
    return order_statistics


def print_order_statistics(order_statistics):
    total, percentage = order_statistics
    print("\nOrder Statistics")
    print(f"Total Products Ordered: {total}")
    print(f"Percentage of Unique Products Ordered: {percentage:.2f}%")


def print_updated_inventory(inventory):
    print("\nUpdated Inventory")
    for product, quantity in inventory.items():
        print(f"{product}: {quantity}")


# Program execution
inventory = initialize_inventory(products)
customer_orders = get_customer_orders()
update_inventory(customer_orders, inventory)
order_statistics = calculate_order_statistics(customer_orders, products)

print_order_statistics(order_statistics)
print_updated_inventory(inventory)