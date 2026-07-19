prices = {"AAPL": 180, "TSLA": 250, "GOOG": 150, "MSFT":400}
def track_protfolio():
    print("--- Stock Portfolio Tracker ---")
    stock = input("Enter stock symbol").strip().upper()
         
    if stock in prices:
        try:
            quantity = int(input(f"Enter quantity  {stock} owned:"))
            total_value = quantity * prices[stock]

            result = f"Total invesment in {stock}: ${total_value}"
            print(f"\n{result}")

            with open ("protfolio.txt", "w") as f:
                f.write(result)
                print("Result saved to portfolio.txt")

        except ValueError:
            print("Invalid input. please enter a number of quantity.")
    else:
        print("Stock symbol not found in our database.")
if __name__ == "__main__":
    track_protfolio()