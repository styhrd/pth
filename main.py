

foods =  []
prices = []
total = 0 


while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q": 
        break
    else:
        price = float(input("Enter Price: "))
        prices.append(price)
        foods.append(food)

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price


print (f"\nTotal Price: {total}")