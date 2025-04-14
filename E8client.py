import Pyro4

uri = input("Enter the Pyro URI of the ListProcessor: ").strip()
processor = Pyro4.Proxy(uri)

client_id = input("Enter your unique client ID: ").strip()

while True:
    print("\nChoose a list operation:")
    print("1. Reverse List")
    print("2. Remove Duplicates")
    print("3. Quit")

    choice = input("Enter choice (1-3): ").strip()
    if choice == "3":
        print("Goodbye!")
        break

    raw_input = input("Enter a comma-separated list (e.g. a,b,b,c): ").strip()
    input_list = [item.strip() for item in raw_input.split(",")]

    if choice == "1":
        result = processor.reverse_list(client_id, input_list)
        print("Reversed List:", result)
    elif choice == "2":
        result = processor.remove_duplicates(client_id, input_list)
        print("List without duplicates:", result)
    else:
        print("Invalid choice.")
