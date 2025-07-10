temperatures = []

for month in range(1, 13):
    temp = int(input(f"Enter the temperature for Month {month}: "))
    temperatures.append(temp)

highest = max(temperatures)
lowest = min(temperatures)

print("\nSummary of the Year:")
print(f"The highest temperature is {highest}°")
print(f"The lowest temperature is {lowest}°")