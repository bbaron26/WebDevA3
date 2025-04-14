import Pyro4

@Pyro4.expose
class Greeter(object):
    def __init__(self):
        self.greeted_names = []

    def greet(self, name):
        self.greeted_names.append(name)
        print(f"greet() called with name: {name}")
        return f"Hello, {name}!"

    def get_history(self):
        print("get_history() called")
        return self.greeted_names

daemon = Pyro4.Daemon()

uri = daemon.register(Greeter)

print("Ready. Object uri =", uri)

daemon.requestLoop()
