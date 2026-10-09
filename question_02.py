def main():
    print("=" * 65)
    print("           ASSIGNMENT 02 - QUESTION # 02 SOLUTION           ")
    print("=" * 65)

    # Dictionary representing store inventory with quantity and unit price
    inventory = {
        "Laptop": {"quantity": 10, "price": 1200.00},
        "Smartphone": {"quantity": 25, "price": 750.50},
        "Wireless Mouse": {"quantity": 60, "price": 25.00},
        "Mechanical Keyboard": {"quantity": 40, "price": 85.00},
        "Gaming Monitor": {"quantity": 15, "price": 320.00},
        "USB-C Cable": {"quantity": 100, "price": 12.50},
    }

    print("\n--- Current Inventory Data ---")
    print(f"{'Item Name':<22} | {'Quantity':<10} | {'Unit Price ($)':<15}")
    print("-" * 55)
    for item, info in inventory.items():
        print(f"{item:<22} | {info['quantity']:<10} | ${info['price']:<14.2f}")

    # =========================================================================
    # Part 1: Loop that iterates through the dictionary and prints each item
    #         along with its quantity in the inventory.
    # =========================================================================
    print("\n" + "=" * 65)
    print("PART 1: Each Item Along with Its Quantity in Inventory")
    print("=" * 65)

    for item, info in inventory.items():
        print(f"Item: {item:<22} --> Quantity: {info['quantity']}")

    # =========================================================================
    # Part 2: Loop that calculates and prints the total value of the inventory
    #         (quantity * price) for all items.
    # =========================================================================
    print("\n" + "=" * 65)
    print("PART 2: Total Inventory Value Calculation (quantity * price)")
    print("=" * 65)

    total_inventory_value = 0.0

    print(f"{'Item Name':<22} | {'Quantity':<10} | {'Price ($)':<12} | {'Total Value ($)':<15}")
    print("-" * 65)

    for item, info in inventory.items():
        quantity = info["quantity"]
        price = info["price"]
        item_total_value = quantity * price
        total_inventory_value += item_total_value

        print(
            f"{item:<22} | {quantity:<10} | ${price:<11.2f} | ${item_total_value:<14.2f}"
        )

    print("-" * 65)
    print(f"Total Value of All Inventory Items: ${total_inventory_value:,.2f}")
    print("=" * 65 + "\n")


if __name__ == "__main__":
    main()
