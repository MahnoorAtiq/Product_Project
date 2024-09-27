# SP23-BAI-023
# SP23-BAI-016
class Product:
  def _init_(self, name, amount, price):
      self.name=name
      self.amount=amount
      self.price=price
    
  def get_price(self, quantity):
        try:
            if quantity<=0:
                raise ValueError("Quantity must be greater than zero.")
            elif quantity<10:
                discount = 0
            elif 10<=quantity < 100:
                discount=0.10 
            else:
                discount=0.20
            total_price = quantity * self.price * (1 - discount)
            return total_price
         except ValueError as e:
            print(f"Error: {e}")
            return None

  def make_purchase(self, quantity):
        if quantity<=0:
            raise ValueError("Quantity must be positive.")
        if quantity>self.amount:
            raise ValueError("Not enough stock to complete the purchase.")
        total_price=self.get_price(quantity)
        # Reduce stock by purchased quantity
        self.amount-=quantity 
        print(f"Purchase successful. Total price: ${total_price}. Remaining stock: {self.amount}.")
try:
        #Attempt to purchase products
        product1 = Product("Coffee Beans", 200, 12.99)
        product1.make_purchase(500) 
        product1.make_purchase(5)    
        product1.make_purchase(100) 
        product1.make_purchase(-5) 
        product2 = Product("Tea Leaves", 100, 5.49)
        product2.make_purchase(10) 
        product2.make_purchase(101)
        product3 = Product("Sugar", 500, 2.99)
        product3.make_purchase(1)
        product3.make_purchase(600)
except ValueError as e:
        print(f"Purchase failed: {e}")

