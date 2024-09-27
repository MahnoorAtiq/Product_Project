#Maintainer's Reg No: SP23-BAI-023
# Collaborator's Reg No: SP23-BAI-016
class Product:
  def _init_(self, name, amount, price):
      self.name=name
      self.amount=amount
      self.price=price

  def get_price(self, quantity):
      def get_price(self, quantity):
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")
            elif quantity < 10:
                discount = 0
            elif 10 <= quantity < 100:
                discount = 0.10  # 10% discount
            else:
                discount = 0.20  # 20% discount
            
            total_price = quantity * self.price * (1 - discount)
            return total_price
        
        except ValueError as e:
            print(f"Error: {e}")
            return None

  def make_purchase(self, quantity):
     pass