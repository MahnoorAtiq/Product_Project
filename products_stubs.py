#Maintainer's Reg No: SP23-BAI-023
# Collaborator's Reg No: SP23-BAI-016
class Product:
  def _init_(self, name, amount, price):
      self.name=name
      self.amount=amount
      self.price=price

  def get_price(self, quantity):
      pass

  def make_purchase(self, quantity):
    try:
        if quantity<=0:
            raise ValueError("Quantity must be positive.")
        if quantity>self.amount:
            raise ValueError("Not enough stock to complete the purchase.")
        total_price=self.get_price(quantity)
        # Reduce stock by purchased quantity
        self.amount-=quantity 
        print(f"Purchase successful. Total price: ${total_price}. Remaining stock: {self.amount}.")
    except ValueError as e:
        print(f"Purchase failed: {e}")