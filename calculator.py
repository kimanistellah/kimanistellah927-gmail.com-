def calculate_discount(price, discount_percent):
    """
    Returns price after applying discount if discount_percent >= 20,
    otherwise returns the original price.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

# Prompt user
try:
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
except ValueError:
    print("Please enter numeric values.")
    exit()

# Calculate and display
final_price = calculate_discount(original_price, discount_percentage)

if discount_percentage >= 20:
    print(f"Discount applied! Final price: ${final_price:.2f}")
else:
    print(f"No discount applied. Price stays: ${final_price:.2f}")