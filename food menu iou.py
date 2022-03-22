    # cafeteria menu
print("Welcome to the Salty Splatoon!")

print(" ")   # spacing for visuals

coffee = int(input("How many coffees would you like today? "))
donut = int(input("How many donuts would you like today? "))
sandwich = int(input("How many sandwiches would you like today? "))
salad = int(input("How many salads would you like today? "))
water = int(input("How many waters would you like today? "))

# Test items: 3 coffee  2 donut 2 sammiches 2 salada 2 wotor
# Total should amount to $24.75

print(" ")   # spacing for visuals

    # calculation part
print("Your total for {0} salads, {1} coffees, {2} donuts, {3} sandwiches, and {4} waters is $" + \
    str((coffee * 1.75) + (donut * 1) + (salad * 5) + (sandwich * 2.75) + (water * 1)).format(salad, coffee, donut, sandwich, water))
