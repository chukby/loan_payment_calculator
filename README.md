# Loan Payment Calculator

A command-line application that calculates monthly payments, total amount paid, and total interest for car loans.

## Features

- **Flexible Loan Calculation**: Calculate monthly payments based on loan amount, interest rate, and duration
- **Down Payment Support**: Optionally deduct a down payment from the initial loan amount
- **Interest Rate Handling**: Supports both 0% and variable interest rates
- **Input Validation**: Robust validation for numerical inputs with user-friendly error messages
- **Detailed Output**: Displays comprehensive loan details including payment breakdown

## Requirements

- Python 3.11 or higher

## Installation

1. Clone or download this repository
2. Ensure you have Python 3.11+ installed
3. No external dependencies required

## Usage

Run the application:

```bash
python main.py
```

The program will prompt you to enter:
1. Total loan amount for the car
2. Annual interest rate (as a percentage, e.g., 7.5 for 7.5%)
3. Loan duration in years
4. Optional down payment amount

The calculator will then display:
- Initial loan amount
- Down payment (if applicable)
- Loan amount after down payment
- Interest rate
- Loan duration
- Monthly payment amount
- Total amount paid over the life of the loan
- Total interest paid

## Example

```
Welcome to the Car Loan Calculator!

Enter the total loan amount for the car: $25000
Enter the annual interest rate (e.g., 7.5 for 7.5%): 6.5
Enter loan duration in years: 5
Do you want to include a down payment? (y/n): y
Enter the down payment amount: $5000

LOAN DETAILS
==================================================
Initial Loan Amount:     $25,000.00
Down Payment:            $5,000.00
Loan Amount:             $20,000.00
Interest Rate:           6.50%
Loan Duration:           5 years (60 payments)
Monthly Payment:         $386.56
Total Amount Paid:       $23,193.36
Total Interest Paid:     $3,193.36
==================================================
```

## License

This project is open source and available for personal and educational use.