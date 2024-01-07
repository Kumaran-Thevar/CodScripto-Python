class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        self.items.append({"product": product, "quantity": quantity})

    def calculate_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        return total


class ECommerceManager:
    def __init__(self):
        self.products = []
        self.shopping_cart = ShoppingCart()

    def display_products(self):
        print("Available Products:")
        for product in self.products:
            print(f"{product.id}. {product.name} - ${product.price}")

    def add_product(self, product):
        self.products.append(product)

    def run(self):
        while True:
            print("\n1. Display Products")
            print("2. Add Product to Cart")
            print("3. View Cart")
            print("4. Checkout")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_products()

            elif choice == "2":
                self.display_products()
                product_id = int(input("Enter product ID to add to cart: "))
                quantity = int(input("Enter quantity: "))
                selected_product = next((p for p in self.products if p.id == product_id), None)
                if selected_product:
                    self.shopping_cart.add_item(selected_product, quantity)
                    print(f"{quantity} {selected_product.name}(s) added to the cart.")

            elif choice == "3":
                print("\nShopping Cart:")
                for item in self.shopping_cart.items:
                    print(f"{item['product'].name} - Quantity: {item['quantity']}")
                print(f"Total: ${self.shopping_cart.calculate_total()}")

            elif choice == "4":
                print("\nCheckout:")
                print(f"Total amount: ${self.shopping_cart.calculate_total()}")
                print("Thank you for shopping with us!")
                break

            elif choice == "5":
                print("Exiting the program.")
                break

            else:
                print("Invalid choice. Please try again.")


# Example usage:
if __name__ == "__main__":
    manager = ECommerceManager()
    manager.add_product(Product(1, "Laptop", 1000))
    manager.add_product(Product(2, "Smartphone", 500))
    manager.add_product(Product(3, "Headphones", 50))

    manager.run()
