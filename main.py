menu = {
    "pizza" : 13.00,
    "nachos" : 7.00,
    "hotdog" : 12.50,
    "chips" : 6.00,
    "lemonade" : 3.20,
}

cart = []
total = 0


print("------MENU------")
for key,value in menu.items():
    print(f"{key:10}: {value: .2f}")
print("----------------")

while True:
    food = input("Enter Food press q to quit: ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += menu.get(food)

for food in cart:
    print (food)

print(total)