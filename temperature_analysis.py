# Name: Jaya Devi S
# Roll Number: iitp_aimltn_2602830
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
max = temperatures[0]
min = temperatures[0]

for temp in temperatures:
    if temp > max:
        max = temp
    if temp < min:
        min = temp

print(f"Highest Temperature: {max}°C")
print(f"Lowest Temperature: {min}°C")


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
count = 0

for temp in temperatures:
  if temp > 30:
    count += 1
  else:
    continue

print(f"Hot Days (>30°C): {count}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
temperatures = [28, 32, 35, 40, 31, 33, 30]
count = 0
day = 0

for temp in temperatures:
    day += 1
    if temp >= 40:
        print(f"Hot Days before alert: {count}")
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day}")
        break
    if temp > 30:
        count += 1
