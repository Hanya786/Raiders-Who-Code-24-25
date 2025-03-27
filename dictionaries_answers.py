
### PROBLEM 1 !!
### i have 3 dogs, 2 cats, and 7 parrots. create a dictionary to reflect this.

# starting code
my_animals = {"dogs": 3, "cats": 2, "parrots": 7}

### once you've done that, add another dog to the dictionary.
my_animals["dogs"] += 1

### then, add a new animal to the dictionary: a zebra.
my_animals["zebras"] = 1

print(my_animals)

### PROBLEM 2 !!
### i have a list of a bunch of crayons. keep track of each colour i have and how many crayons of that colour i have.
box_of_crayons = ["red", "blue", "red", "red", "orange", "orange", "yellow", "cyan", "blue", "orange", "yellow", "purple", "black", "white", "green", "turquoise", "indigo", "fuscia", "orange", "plum", "grey"]

### hint: use a for loop.
crayons = {}
for colour in box_of_crayons:
  if colour in crayons:
    crayons[colour] += 1
  else:
    crayons[colour] = 1

print(crayons)

### PROBLEM 3 !! this one is diffucult
### you own a clothing store. you sell t-shirts, pants, and socks. each t-shirt is $15, each pair of patns is $20, and each pair of socks is $5.
### a bunch of customers are coming in with requests of what clothes they want and how many. you must tell them the total price of their purchase.
### hint: use a dictionary to keep track of your prices. use a dictionary to keep track of stock as well.
### once you run out of stock, be sure to ONLY GIVE THE CUSTOMER THE PRICE OF WHAT THEY CAN BUY (don't include the price of the t-shirt they want if there are none in stock).

def clothing_store():
  # here are the customers:
  customers = [["3 t-shirts", "8 pants", "10 socks"], ["6 t-shirts", "1 pants", "4 socks"],["8 t-shirts", "12 pants", "3 socks"]]

  ### these two dictionaries can be merged together if you'd like! lists can be values. values do not have to be integers.
  clothing = {"t-shirts":100, "pants":20,"socks":11}
  clothing_cost = {"t-shirts":15, "pants":20, "socks":5}

  for customer in customers:
    print(customer) # this is for testing / to show progress
    price = 0
    for item in customer:
      item = item.split(" ")
      if clothing[item[1]] >= int(item[0]):
        price += int(item[0]) * clothing_cost[item[1]]
        clothing[item[1]] -= int(item[0])
      else:
        price += clothing[item[1]] * clothing_cost[item[1]]
        clothing[item[1]] = 0
    print(clothing) # this is for testing / to show progress
  
    print(price) # this is for testing / to show progress

clothing_store()







  
