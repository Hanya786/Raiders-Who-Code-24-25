### dictionaries are a type of array in Python. 

### they have KEYS and VALUES.

### for example: 

# demonstrates the amount of each fruit we have. the FRUIT NAME is the KEY and the NUMBER OF FRUIT is the VALUE.
my_food = {"apple":3, "banana":2, "orange":7}

# this prints the number of apples.
print(my_food["apple])

# this prints all the fruits in our dictionary.
for food in my_food:
  # this prints the food. aka the key
  print(food)
  # this prints the value. aka the amount
  print(my_food[food])

### PROBLEM 1 !!
### i have 3 dogs, 2 cats, and 7 parrots. create a dictionary to reflect this.

# starting code
my_animals = {}

### once you've done that, add another dog to the dictionary.

### then, add a new animal to the dictionary: a zebra.

### PROBLEM 2 !!
### i have a list of a bunch of crayons. keep track of each colour i have and how many crayons of that colour i have.
box_of_crayons = ["red", "blue", "red", "red", "orange", "orange", "yellow", "cyan", "blue", "orange", "yellow", "purple", "black", "white", "green", "turquoise", "indigo", "fuscia", "orange", "plum", "grey"]

### hint: use a for loop.
crayons = {}

### PROBLEM 3 !! this one is diffucult
### you own a clothing store. you sell t-shirts, pants, and socks. each t-shirt is $15, each pair of patns is $20, and each pair of socks is $5.
### a bunch of customers are coming in with requests of what clothes they want and how many. you must tell them the total price of their purchase.
### hint: use a dictionary to keep track of your prices. use a dictionary to keep track of stock as well.
### once you run out of stock, be sure to ONLY GIVE THE CUSTOMER THE PRICE OF WHAT THEY CAN BUY (don't include the price of the t-shirt they want if there are none in stock).

def clothing_store():
  # here are the customers:
  customers = [["3 t-shirts", "8 pants", "10 socks"], ["6 t-shirts", "1 pants", "4 socks"],["8 t-shirts", "12 pants", "3 socks"]]
  clothing = {"t-shirts":100, "pants":20,"socks":11}

clothing_store()







  

