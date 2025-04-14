import Pyro4

lb = Pyro4.Proxy("PYRONAME:load_balancer")

while True:
    print("\nOptions:")
    print("1. Calculate Mean")
    print("2. Calculate Median")
    print("3. Quit")
    choice = input("Choose (1-3): ")

    if choice == "3":
        break

    raw = input("Enter comma-separated numbers (e.g., 1,2,3): ")
    try:
        numbers = [float(n.strip()) for n in raw.split(",")]
    except ValueError:
        print("Invalid number list.")
        continue

    if choice == "1":
        print("Result:", lb.forward_mean(numbers))
    elif choice == "2":
        print("Result:", lb.forward_median(numbers))
    else:
        print("Invalid choice.")
