radius = 84
pi = 3.14
water_per_square_meter = 1.4

# Calculate area
area = pi * radius * radius

# Calculate total water
water = area * water_per_square_meter

print("Pond area:", area)
print("Total water:", int(water))
