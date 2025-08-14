# Create a function named calculate_discount(price, discount_percent) that calculates 
# the final price after applying a discount. The function should take the original price 
# (price) and the discount percentage (discount_percent) as parameters. If the discount 
# is 20% or higher, apply the discount; otherwise, return the original price.


def calculate_discount(price, discount_percent):

    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount must be non-negative.")
    if discount_percent < 0.2:
        return price
    else:
        return price * (1 - discount_percent)

# Using the calculate_discount function, prompt the user to enter the original price of 
# an item and the discount percentage. Print the final price after applying the discount, 
# or if no discount was applied, print the original price.


original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage (as a decimal): "))

print(f"Final price for the item: Ksh. {calculate_discount(original_price, discount_percentage):.2f}")