import math

# wavelength thing 
freq = int(input ("Enter the value in MHZ: "))
meter = str(3e8 / (freq * 1e6))
# 1e6 is equivalent to 1×10⁶ 
print("For a given frequency of", freq, "MHz, the wavelength is", meter, "m.")

# area & circumfrence of circle 
radius = int(input ("Enter radius given in cm: "))
circum = round(2 * math.pi * radius)
area = round(math.pi * radius ** 2)
print("The circumfrence is", circum, "cm, and the area is", area, "cm.")