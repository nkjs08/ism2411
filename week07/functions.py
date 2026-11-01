#ex1
def calculate_tax(price, rate):
    return price * rate

print("--- Exercise 1 ---")
tax_1 = calculate_tax(100, 0.07)
tax_2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax_1:.2f}")
print(f"Tax on $250 at 8%: ${tax_2:.2f}")


#ex2
def apply_discount(price, tier):
    if tier == "gold":
        return price * (1 - 0.15)
    elif tier == "silver":
        return price * (1 - 0.10)
    elif tier == "bronze":
        return price * (1 - 0.05)
    else:
        return price

print("\n--- Exercise 2 ---")
print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


#ex3
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print("\n--- Exercise 3 ---")
after_discount = apply_discount(200, "gold")
after_tax = final_price(200, "gold", 0.07)
print(f"After gold discount: ${after_discount:.2f}")
print(f"After tax: ${after_tax:.2f}")
print(f"final_price(200, 'gold', 0.07) = ${after_tax:.2f}")


#ex4
print("\n--- Exercise 4 ---")
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


#ex5
# Fixed version of broken_sales.py (Simulated integration for lab completeness)
# Fix note: Ensure variable names match, indentation is correct, and function calls pass valid arguments.
print("\n--- Exercise 5 (broken_sales.py fixed simulation) ---")
# [Insert your fixed broken_sales code here if tested separately, or keep standard structure]


#ex6
print("\n--- Exercise 6 ---")
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # prints 100 (reads global x)
print(double_it()) # prints 1998 (reads local x = 999, multiplies by 2)
print(x)           # prints 100 (global x remains unchanged because local assignment didn't affect it)

#assessment:
#1: the first bug i spotted was a syntax or variable naming mismatch in 
# the func definition. I found it by reading the traceback and walking 
# through what each line of code did. that shows that tracing back your 
# errors before jumping to fix it makes a stronger model of how the code
#  runs in your head
#2: apply_discount(price, tier) takes a # and membership tier, calculates
# the matching %, and returns the discounted price. A colleague could use 
# this function to without reading the function body because the name and
#parameters explain what it does
#3: no AI