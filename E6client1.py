import Pyro4

uri = input("Enter the Pyro URI of the Greeter class: ").strip()
name = input("What is your name? ").strip()

greeter = Pyro4.Proxy(uri)

print(greeter.greet(name))

