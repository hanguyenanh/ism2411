# Question 1: The first bug I spotted was the SyntaxError, because of the missing colon in the for loop. I found it from the traceback.
# The second one was the IndexError, which named line 16 and the error type right away.
# The wrong total (Total: $90) was harder, because it produced no error, and I only caught it by checking the output against what the five sales should add up to.
# This tells me my current debugging instincts are strong at reading tracebacks but weaker at noticing silent logic errors,
# since those only show up when I trace values with print() statements and compare them to what I expected.
# My next step is to check the output for correctness as a habit, not just wait for a crash. 

# Question 2: apply_discount(price, tier) takes a price (a number) and a membership tier (a string such as "gold", "silver", or "bronze") and returns the price after the tier's discount: 15% off for gold, 10% for silver, and 5% for bronze. 
# Any other tier, like "none", returns the price unchanged. It only returns a value and doesn't print anything or change its inputs. 
# A colleague could mostly use it without reading the body, but there is no docstring listing the valid tiers, 
# and a typo like "Gold" would silently return the full price instead of raising an error. Adding a one-line docstring would close that gap.

# Question 3:
# AI disclosure: I used Claude in Exercise 5 to explain the IndexError and check my fixes, and for sample wording on the Exercise 5 write-up as well.
# Its explanation of the IndexError helped me see why a <= loop reaches an index that doesn't exist.

# Exercise 1

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier =="silver":
        return price * 0.90
    elif tier=="bronze":
        return price * 0.95
    else:
        return price

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3

def final_price(price, discount_tier, tax_rate):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

discounted = apply_discount(200, "gold")
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${discounted + calculate_tax(discounted, 0.07):.2f}")
print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, tier, rate)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# Exercise 5

# Bug 1: the for loop was missing a colon at the end of the line.
# Bug 2: the while loop used i <= len(sales), so i went one past the last index and caused an IndexError.
# Bug 3: the loop had total = sale, which replaced total with the current sale in every pass, so the result was just sale instead of the sum.

sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    # Fix: use += so each sale is added to the running total instead of replacing it
    total += sale 
print(f"Total: ${total}") # Total: $715

count = 0 
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
# Fix: use < so i stops at 4, the last valid index in a 5-item list
while i < len(sales):
    print(sales[i])
    i += 1

# Exercise 6

# Scope: a variable assigned inside a function is local to that function
# The x = 999 inside double_it() is a separate variable from the global x = 100,
# so calling the function never changes the global x.

x = 100

def double_it():
    x = 999
    return x * 2

print(x) # 100
print(double_it()) # 1998
print(x) # 100, unchanged