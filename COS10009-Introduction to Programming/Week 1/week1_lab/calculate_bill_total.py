# Complete the three missing lines of code below

def main():
    print("Enter the appetizer price:")
    appetizer_price = float(input())

    # complete the code below using appetizer_price
    # above as an example then uncomment the line:
    print("Enter the main price:")
    # main_price =
    main_price = float(input())
    # complete the code below using appetizer_price
    # above and uncomment the line: 
    print("Enter the dessert price:")
    # dessert_price =
    desser_price = float(input())
    # Add up the price for the appetizer, main and dessert
    # total_price =
    total_prize = appetizer_price + main_price + desser_price
    # format the float to 2 decimal places and print it out
    print(f"The total prize is ${total_prize:.2f}. ")

if __name__ == "__main__":
    main()