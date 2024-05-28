# Get user details
name = input("Enter your name: ")
gender = input("Enter your gender (Male/Female): ")
age = int(input("Enter your age: "))

# Get purchase details
product = input("Enter product : ")
product_gram = float(input("Enter product gram: "))
current_gold_price_per_gram = 57522  # Given gold price

# Calculate total gold rate
total_gold_rate = product_gram * current_gold_price_per_gram

# Making charges
making_charges_per_gram = 845  # Given making charges
total_making_charges = product_gram * making_charges_per_gram

# Calculate total amount before discount
total_amount = total_gold_rate + total_making_charges

# Determine discount percentage based on user details
discount_percentage = 0
if gender == "Male":
    if age > 65:
        if total_gold_rate > 500000:
            discount_percentage = 35
        elif total_gold_rate > 300000:
            discount_percentage = 30
        elif total_gold_rate > 200000:
            discount_percentage = 20
    else:
        if total_gold_rate > 500000:
            discount_percentage = 25
        elif total_gold_rate > 300000:
            discount_percentage = 20
        elif total_gold_rate > 200000:
            discount_percentage = 10
elif gender == "Female":
    if age > 65:
        if total_gold_rate > 500000:
            discount_percentage = 40
        elif total_gold_rate > 300000:
            discount_percentage = 35
        elif total_gold_rate > 200000:
            discount_percentage = 25
    else:
        if total_gold_rate > 500000:
            discount_percentage = 30
        elif total_gold_rate > 300000:
            discount_percentage = 25
        elif total_gold_rate > 200000:
            discount_percentage = 15
print(discount_percentage)
# Calculate discount amount and total net amount
discount_amount = (total_gold_rate * discount_percentage) / 100
total_net_amount = total_amount - discount_amount

# Display the details and calculated amounts
print("-------------------------------------------------------------------------")
print("KALYAN JEWELLERS")
print("-------------------------------------------------------------------------")
print(f"Customer Name: {name}")
print(f"Gender: {gender}")
print(f"Age: {age}")
print(f"Product: {product}")
print(f"Product Gram: {product_gram} grams")
print(f"Current Gold Price (per gram): {current_gold_price_per_gram}")
print("-------------------------------------------------------------------------")
print(f"TOTAL GOLD RATE: {total_gold_rate:.2f}")
print(f"Making Charges (per gram): {making_charges_per_gram}")
print(f"Total Making Charges: {total_making_charges:.2f}")
print("-------------------------------------------------------------------------")
print(f"TOTAL AMOUNT: {total_amount:.2f}")
print(f"DISCOUNT: {discount_percentage}%")
print(f"DISCOUNT AMOUNT: {discount_amount:.2f}")
print("-------------------------------------------------------------------------")
print(f"TOTAL NET AMOUNT: {total_net_amount:.2f}")
print("-------------------------------------------------------------------------")
