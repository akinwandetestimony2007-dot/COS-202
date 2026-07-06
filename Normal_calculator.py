def calculator():

    print("=" * 45)

    print("      MATHEMATICAL CALCULATOR (MC)")

    print("=" * 45)

    while True:

        print("\nAvailable Operations")

        print("+  Addition")

        print("-  Subtraction")

        print("*  Multiplication")

        print("/  Division")

        print("\\  Floor Division")

        print("^  Power")

        print("%  Modulus")

        print("C  Clear")

        print("OFF  Exit Calculator")

        choice = input("\nEnter Operation: ").upper()

        if choice == "OFF":

            print("Calculator Closed.")

            break

        elif choice == "C":

            print("\n" * 50)

            continue

        elif choice in ["+", "-", "*", "/", "\\", "^", "%"]:

            try:

                num1 = float(input("Enter First Number: "))

                num2 = float(input("Enter Second Number: "))

                if choice == "+":

                    result = num1 + num2

                elif choice == "-":

                    result
