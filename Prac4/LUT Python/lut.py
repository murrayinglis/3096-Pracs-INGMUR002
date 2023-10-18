import math
import numpy as np

# Define the number of points in the lookup table
num_points = 128*4

# Create the lookup table for the sinusoid
sinusoid_lut = []
for i in range(num_points):
    value = round(511 * (1 + math.sin(2 * math.pi * i / num_points)))
    sinusoid_lut.append(value)

# Create the lookup table for the sawtooth wave
sawtooth_lut = np.linspace(0, 1023, num_points, endpoint=False).astype(int).tolist()

# Create the lookup table for the triangular wave
triangular_lut = []
for i in range(num_points):
    value = int((1023 / (num_points / 2)) * (num_points / 2 - abs(i - num_points / 2)))
    triangular_lut.append(value)

# Print the lookup tables
print("Sinusoid Lookup Table: ", sinusoid_lut)
print("\nSawtooth Wave Lookup Table: ", sawtooth_lut)
print("\nTriangular Wave Lookup Table: ", triangular_lut)
