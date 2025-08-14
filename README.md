[No content]
# PLP Week 3 Python Assignment

## Overview
This assignment demonstrates how to calculate the final price of an item after applying a discount using Python. The program prompts the user for the original price and the discount percentage, then calculates and displays the final price based on the discount rules.

## Features
- Defines a function `calculate_discount(price, discount_percent)` to compute the discounted price.
- Applies the discount only if the percentage is 20% (0.2) or higher; otherwise, returns the original price.
- Handles invalid input by raising a `ValueError` if negative values are entered.
- Interactive user input for price and discount percentage.
- Displays the final price in Kenyan Shillings (Ksh).

## Usage
1. Run the script `discount.py`.
2. Enter the original price of the item when prompted.
3. Enter the discount percentage as a decimal (e.g., 0.2 for 20%).
4. The program will display the final price after applying the discount.

### Example
```
Enter the original price of the item: 1000
Enter the discount percentage (as a decimal): 0.25
Final price for the item: Ksh. 750.00
```

## Function Details
### calculate_discount(price, discount_percent)
- **Parameters:**
  - `price` (float): The original price of the item.
  - `discount_percent` (float): The discount rate as a decimal (e.g., 0.2 for 20%).
- **Returns:**
  - The price after applying the discount if the discount is 20% or higher.
  - The original price if the discount is less than 20%.
- **Raises:**
  - `ValueError` if either `price` or `discount_percent` is negative.

## Requirements
- Python 3.x

## Notes
- Ensure you enter the discount as a decimal (e.g., 0.2 for 20%).
- The program does not handle non-numeric input.

## License
This project is for educational purposes.
