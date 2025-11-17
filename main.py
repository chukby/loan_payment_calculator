
def get_positive_float(prompt):
    """Get positive float input from user with validation."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_positive_int(prompt):
    """Get positive integer input from user with validation."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def main():
      """
      This program calculates the monthly payment, total amount paid,
      and total interest paid on a car loan based on user inputs.
      """
      print("\n" + "="*50)
      print("Welcome to the Car Loan Calculator!")      
      print("="*50 + "\n")
      
      initial_loan_amount = get_positive_float("Enter the total loan amount for the car: $")
      annual_interest_rate = get_positive_float("Enter the annual interest rate (e.g., 7.5 for 7.5%): ")
      loan_duration = get_positive_int("Enter loan duration in years: ")
    
      down_payment_choice = input("Do you want to include a down payment? (y/n): ").strip().lower()
    
      if down_payment_choice in ["yes", "y"]:
        down_payment_amount = get_positive_float("Enter the down payment amount: $")
        loan_amount = initial_loan_amount - down_payment_amount
      else:
        loan_amount = initial_loan_amount
        down_payment_amount = 0
    
      total_payments = loan_duration * 12
    
     # Handle both 0% and non-0% interest rates
      if annual_interest_rate == 0:
          monthly_payment = loan_amount / total_payments
      else:
          monthly_interest_rate = annual_interest_rate / 1200
          numerator = loan_amount * monthly_interest_rate
          denominator = 1 - (1 + monthly_interest_rate) ** (-total_payments)
          monthly_payment = numerator / denominator
    
          total_paid = monthly_payment * total_payments
          total_interest = total_paid - loan_amount

      print("\n" + "="*50)
      print("LOAN DETAILS")
      print("="*50)
      print(f"Initial Loan Amount:     ${initial_loan_amount:,.2f}")
      print(f"Down Payment:            ${down_payment_amount:,.2f}")
      print(f"Loan Amount:             ${loan_amount:,.2f}")
      print(f"Interest Rate:           {annual_interest_rate:.2f}%")
      print(f"Loan Duration:           {loan_duration} years ({total_payments} payments)")
      print(f"Monthly Payment:         ${monthly_payment:,.2f}")
      print(f"Total Amount Paid:       ${total_paid:,.2f}")
      print(f"Total Interest Paid:     ${total_interest:,.2f}")
      print("="*50 + "\n")


if __name__ == "__main__":
    main()
