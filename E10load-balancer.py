import Pyro4

@Pyro4.expose
class LoadBalancer:
    counter = 0

    def __init__(self):
        self.stats1 = Pyro4.Proxy("PYRONAME:stats1")
        self.stats2 = Pyro4.Proxy("PYRONAME:stats2")

    def forward_mean(self, numbers):
        if LoadBalancer.counter % 2 == 0:
            result = self.stats1.calculate_mean(numbers)
            source = "stats1"
        else:
            result = self.stats2.calculate_mean(numbers)
            source = "stats2"
        LoadBalancer.counter += 1
        print(f"LoadBalancer: Forwarded mean to {source}")
        return f"{result} (from {source})"

    def forward_median(self, numbers):
        if LoadBalancer.counter % 2 == 0:
            result = self.stats1.calculate_median(numbers)
            source = "stats1"
        else:
            result = self.stats2.calculate_median(numbers)
            source = "stats2"
        LoadBalancer.counter += 1
        print(f"LoadBalancer: Forwarded median to {source}")
        return f"{result} (from {source})"

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(LoadBalancer)
ns.register("load_balancer", uri)
print("LoadBalancer is live.")
daemon.requestLoop()
