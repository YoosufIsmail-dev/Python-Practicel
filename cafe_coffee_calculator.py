# Café Coffee Price Calculator

price = float(input("Enter coffee price: "))
age = int(input("Enter customer age: "))
loyalty_card = input("Does the customer have a loyalty card? (yes/no): ").lower()

# Age-based discount
if age < 18:
    discount = 20
elif age <= 60:
    discount = 10
else:
    discount = 50

# Additional loyalty card discount
if loyalty_card == "yes":
    discount += 5

# Calculate final price
final_price = price - (price * discount / 100)

print(f"\nTotal Discount: {discount}%")
print(f"Final Price: ${final_price:.2f}")
