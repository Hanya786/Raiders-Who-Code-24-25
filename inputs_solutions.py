
class Restaurant
  def __init__(self):
    self.prices = [1,2,3,40,50,25,43]
    self.menu = ["Water", "Pop", "Crackers", "Burger", "Steak","Pizza", "Rigatoni"]
    #prices correspond to food items in order
  def order(self):
    food = input("Welcome to our restaurant! What would you like to eat today?")
    count = 0
    #count variable is to keep track of which index of the list we are at
    for item in self.menu:
      if food == item:
        price = self.prices[count]
      count +=1
    return "Your price is $" + price + " ! Have a great day."
