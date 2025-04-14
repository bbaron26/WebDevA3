import Pyro4

uri = input("Enter the Pyro URI of the Greeter class: ").strip()
greeter = Pyro4.Proxy(uri)

while True:
    option = input("\nChoose an action: 'greet', 'history', or 'quit': ").strip().lower()

    if option == "greet":
        name = input("Enter a name to greet: ").strip()
        print(greeter.greet(name))

    elif option == "history":
        history = greeter.get_history()
        print("Names greeted so far:", history)

    elif option == "quit":
        print("Goodbye!")
        break

    else:
        print("Invalid input.")

