#PIZZA ORDER CORRECTION.
#First Variation.
#Write a welcom and menu message
print("Welcome to Dominos Pizzarati")
print("""Pizza Cost:
Small Pizza: #4000
Medium Pizza: #6000
Large Pizza: #10000\n""")

print("""Extras:
Pepperoni for Small Pizza: +$1000
Pepperoni for Medium or Large Pizza: + #2000
Extra cheese for any size pizza: + #1000\n""")

#prices
small_pizza = int("4000")
medium_pizza = int('6000')
large_pizza = int('10000')
pepperoni_for_small_pizza = int('1000')
pepperoni_for_medium_or_large_pizza = int('2000')
Extra_cheese_for_any_pizza = int('1000')

#Order combinations
print("""Choices:
1: small pizza only
2: medium pizza only
3: large pizza only
4:Pepperoni for Small Pizza only
5:Pepperoni for Medium or Large Pizza only
6:Extra cheese for any size pizza only\n
----Add Extras----
7:Small Pizza + Pepperoni for Small Pizza: +$1000
8:small pizza + extra cheese #1000
9:medium pizza + Pepperoni for Medium or Large Pizza: + #2000
10:Medium Pizza + extra cheese #1000
11:Large Pizza + Extra cheese for any size pizza: + #1000
12: Quit Order""")
#Choice while loop
while True:
    #Ask user for input
       choice = int(input("Enter choice:"))
       if (choice in [1,2,3,4,5,6,7,8,9,10,11,12]):
           if choice == 12:
                break
#if elif and else statements
           if choice == 1:
               print("your order is small pizza only, cost is #4000")
           elif choice == 2:
               print("your order is medium pizza only, cost is #6000")
           elif choice == 3:
               print("your order is large pizza only, cost is #10000")
           elif choice == 4:
               print("your order is  pepperoni for small pizza only,cost is #1000")
           elif choice == 5:
               print("your order is Pepperoni for Medium or Large Pizza, cost is #2000")
           elif choice == 6:
               print("Extra cheese for any size pizza only, cost is #1000")
               print('The price is: {}'.format(result)) 
           elif choice == 7:
               result = small_pizza + pepperoni_for_small_pizza
               print("Your choice is small_pizza and pepperoni_for_small_pizza")
               print('The price is: {}'.format(result)) 
           elif choice == 8:
               result = small_pizza + Extra_cheese_for_any_pizza
               print("Your choice is small_pizza and Extra_cheese_for_any_pizza")
               print('The price is: {}'.format(result)) 
           elif choice == 9:
               result = medium_pizza + pepperoni_for_medium_or_large_pizza 
               print("Your choice is medium_pizza and pepperoni_for_Medium_or_large_pizza")
               print('The price is: {}'.format(result)) 
           elif choice == 10:
               result = medium_pizza + Extra_cheese_for_any_pizza 
               print("Your choice is medium_pizza and Extra_cheese_for_any_pizza")
               print('The price is: {}'.format(result)) 
           elif choice == 11:
               result = large_pizza + Extra_cheese_for_any_pizza
               print("Your choice is small_pizza and pepperoni_for_small_pizza")
               print('The price is: {}'.format(result)) 
           else:
               print("you have selected an invalid order")
        
                            
#Second Variation.
#Write a welcome messages and menu
print("Welcome to Dominos Pizzarati")
print("""Pizza Cost:
Small Pizza: #4000
Medium Pizza: #6000
Large Pizza: #10000\n""")

print("""Extras:
Pepperoni for Small Pizza: +$1000
Pepperoni for Medium or Large Pizza: + #2000
Extra cheese for any size pizza: + #1000\n""")

#Declare an empty list
pizzas = []
prices = []
total = 0
#Order loop
while True:
#Ask the user for input
    pizza = input("enter a pizaa you want to buy(q to quit):")
    if pizza == "q":
        break
    else:
        price = float(input(f"enter the price of{pizza}: #"))
        pizzas.append(pizza)
        prices.append(price)

print("-----Your cart----")
#Loop to iterate of the user input
for pizza in pizzas:
    print(pizza,end=" ")

#Loop for the price        
for price in prices:
    total+= price

#Pint the out come
print(f"your total is #{total}")

#Variation 3 choose any of the 3
print("Welcome to Dominos Pizzarati")
print("""Pizza Cost:
Small Pizza: #4000
Medium Pizza: #6000
Large Pizza: #10000\n""")

print("""Extras:
Pepperoni for Small Pizza: +$1000
Pepperoni for Medium or Large Pizza: + #2000
Extra cheese for any size pizza: + #1000\n""")
# Prices
small_pizza_price = 4000
medium_pizza_price = 6000
large_pizza_price = 10000
pepperoni_small = 1000
pepperoni_medium_large = 2000
extra_cheese = 1000

# Order loop
ordering = True

while ordering:
    print("Take an order")
    
    # Ask for pizza size
    size = input("Choose pizza size: Small (S), Medium (M), or Large (L): ").lower()

    # Set initial cost based on pizza size
    if size == 's':
        cost = small_pizza_price
        print(f"You chose Small pizza: ${cost}")
    elif size == 'm':
        cost = medium_pizza_price
        print(f"You chose Medium pizza: ${cost}")
    elif size == 'l':
        cost = large_pizza_price
        print(f"You chose Large pizza: ${cost}")
    else:
        print("Invalid size. Please select again.")
        continue

    # Ask if they want pepperoni
    pepperoni = input("Do you want pepperoni? Yes (Y) or No (N): ").lower()
    
    if pepperoni == 'y':
        if size == 's':
            cost += pepperoni_small
            print(f"Added pepperoni for small pizza: +${pepperoni_small}")
        else:
            cost += pepperoni_medium_large
            print(f"Added pepperoni for medium or large pizza: +${pepperoni_medium_large}")
    elif pepperoni != 'n':
        print("Invalid choice for pepperoni. Please select again.")
        continue

    # Ask if they want extra cheese
    cheese = input("Do you want extra cheese? Yes (Y) or No (N): ").lower()
    
    if cheese == 'y':
        cost += extra_cheese
        print(f"Added extra cheese: +${extra_cheese}")
    elif cheese != 'n':
        print("Invalid choice for cheese. Please select again.")
        continue

    # Show total cost
    print(f"Your total cost is: ${cost}")

    # Ask if they want to order again
    another_order = input("Would you like to order another pizza? Yes (Y) or No (N): ").lower()
    
    if another_order == 'n':
        ordering = False
        print("Thank you for your order!")
    elif another_order != 'y':
        print("Invalid input. Exiting the order system.")
        ordering = False
                      
