import Pyro4

uri = input("Enter the Pyro URI of the ArithmeticServer: ").strip()
calc = Pyro4.Proxy(uri)

while True:
    print("\nChoose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Quit")
    
    choice = input("Enter your choice (1-4): ").strip()

    if choice == "4":
        print("Goodbye!")
        break

    a = input("Enter the first number: ").strip()
    b = input("Enter the second number: ").strip()

    if choice == "1":
        print("Result:", calc.add(a, b))
    elif choice == "2":
        print("Result:", calc.subtract(a, b))
    elif choice == "3":
        print("Result:", calc.divide(a, b))
    else:
        print("Invalid option.")
