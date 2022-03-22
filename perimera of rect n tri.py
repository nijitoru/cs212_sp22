import math

print(" ")          # CS212 \ January 20, 2022
print(" ")          # spacing for visuals
print(" ")

# rectangle-chan
print("---   Finding the area and perimeter for rectangle-chan   ---")

widthR = int(input("Enter the length of width in inches: "))
heightR = int(input("Enter the length of height in inches: "))

    # doodle of rectangle-chan
lineR = ("|" + " " * (2 * widthR) + "|")

print("+" + "-" * (2*widthR) + "+")
for i in range(int(heightR / 3)):
    print(lineR)

print("|" + " " * (2*widthR) + "|" + " Height = " + str(heightR), "in")

for i in range(int(heightR / 3)):
    print(lineR)
print("+" + "-" * (2*widthR) + "+")

print("     Width = " + str(widthR), "in")
print("-" * 25)

# perimeter and area of rectangle-chan
areaR = widthR * heightR
print("Area =", areaR, "in" + "\u00B2")

periR = (widthR * 2) + (heightR * 2)
print("Perimeter =", periR, "in.")

print(" ")
print(" ")     # spacing for visuals
print(" ")

# triangle-kun
print("---   Finding the area and perimeter for equilateral triangle   ---")

sideT = int(input("Enter the length of a side in inches: "))

    # semi-perimeter
semP = (sideT * 3) / 2

    # doodle of triangle-kun
for row in range(1, int((sideT + 1))):
    for col in range(1, (2 * sideT)):
        if row == sideT or row+col == sideT + 1 or col - row == sideT - 1:
            print("*", end = "")
        else:
            print(end = " ")
    print()

    # i forgot the formula so i did this instead
    # i knew i had to use importation of the maths guh
        # the actual formula i should've done: 
        # round((math.sqrt(3) / 4) * sideT ** 2)
areaT = round((semP * (semP-sideT) ** 3) ** 0.5)
print("Area =", areaT, "in" + "\u00B2")

periT = sideT * 3
print("Perimeter =", periT, "in.")
