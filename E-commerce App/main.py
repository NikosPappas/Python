from abc import ABC, abstractmethod

class Product:
    def __init__(self, product_id, name, description, price, category=None):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"

    def get_price(self):
        return self.price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity=1):
        for item in self.items:
            if item[0].product_id == product.product_id:
                item[1] += quantity
                return
        self.items.append([product, quantity])

    def remove_item(self, product, quantity=1):
        for item in self.items:
            if item[0].product_id == product.product_id:
                if quantity >= item[1]:
                    self.items.remove(item)
                else:
                    item[1] -= quantity
                return

    def get_total(self):
        total = 0
        for item in self.items:
            total += item[0].get_price() * item[1]
        return total

    def apply_discount(self, discount):
        return discount.apply_discount(self)

    def get_final_total(self):
      return self.get_total() # Discounts are applied in place

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return

        print("Your Cart:")
        for item in self.items:
            print(f"- {item[0]} x {item[1]}")
        print(f"Total: ${self.get_total():.2f}")


class Discount(ABC):
    @abstractmethod
    def apply_discount(self, cart):
        pass  # Abstract method - must be implemented by subclasses


class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, cart):
        total = cart.get_total()
        discount_amount = total * self.percentage
        return total - discount_amount


class FixedAmountDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, cart):
        total = cart.get_total()
        return max(0, total - self.amount) # Ensure total doesn't go below zero

#Example Usage
product1 = Product("P101", "T-Shirt", "A comfortable cotton t-shirt", 20.00)
product2 = Product("P102", "Jeans", "Classic denim jeans", 50.00)
product3 = Product("P103", "Hat", "Stylish baseball cap", 15.00)

cart = ShoppingCart()
cart.add_item(product1, 2)
cart.add_item(product2)
cart.add_item(product3, 3)

cart.display_cart()

percentage_discount = PercentageDiscount(0.10) #10% off
total_with_discount = cart.apply_discount(percentage_discount)
print(f"Total with percentage discount: ${total_with_discount:.2f}")

fixed_discount = FixedAmountDiscount(10)
total_with_fixed_discount = cart.apply_discount(fixed_discount)
print(f"Total with fixed discount: ${total_with_fixed_discount:.2f}")