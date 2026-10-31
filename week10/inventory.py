# Question 1: I expected slicing to work like Excel ranges, where A1:A4 includes the last cell, but in Python my_list[1:4] stops before index 4 and starts counting from 0.
# I was so surprised that my_list[-1] gets the last item with no need to know the list's length, which would be handy for something like pulling the most recent monthly return from a list of returns.

# Question 2: As a treasurer of my high school Psychology club, I tracked dues for about 150 members and sent payment reminders by building a mail merge in Excel by hand, which meant fixing mismatched rows every time the roster changed.
# With a Python list of members, I could have looped through it, filtered out the people who already paid, and generated each personalized reminder automatically.

print("--- Exercise 1: Build a List ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2

print("--- Exercise 2: Index Practice ---")

print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])

# Exercise 3

print("--- Exercise 3: List Slicing ---")

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4

print("--- Exercise 4: List Methods ---")

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try: 
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident")

print(coords)

# Exercise 6

print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

# Exercise 7

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

# Exercise 8

print("--- Exercise 8: Filter ---")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
