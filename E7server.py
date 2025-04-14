import Pyro4

@Pyro4.expose
class ArithmeticServer(object):
    def add(self, a, b):
        print(f"add({a}, {b}) called")
        try:
            return float(a) + float(b)
        except ValueError:
            return "Invalid input: please enter numeric values."

    def subtract(self, a, b):
        print(f"subtract({a}, {b}) called")
        try:
            return float(a) - float(b)
        except ValueError:
            return "Invalid input: please enter numeric values."

    def divide(self, a, b):
        print(f"divide({a}, {b}) called")
        try:
            a = float(a)
            b = float(b)
            if b == 0:
                return "Error: Cannot divide by zero."
            return a / b
        except ValueError:
            return "Invalid input: please enter numeric values."

daemon = Pyro4.Daemon()

uri = daemon.register(ArithmeticServer)

print("Ready. Object uri =", uri)

daemon.requestLoop()
