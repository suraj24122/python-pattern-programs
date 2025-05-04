# diamond pattern

n = 5

for i in range(n):
    for j in range(i, n):  # Adjust spacing for upper part
        print(" ", end=" ") 
    for j in range(i):  # Print left side stars
        print("*", end=" ")
    for j in range(i + 1):  # Print right side stars
        print("*", end=" ")
    print()
for i in range(1, n):  # Start from 1 to avoid repeating the middle row
    for j in range(i + 1):  # Adjust spacing for lower part
        print(" ", end=" ")
    for j in range(i, n - 1):  # Print left side stars
        print("*", end=" ")
    for j in range(i, n):  # Print right side stars
        print("*", end=" ")
    print()