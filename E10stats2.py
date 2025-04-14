import Pyro4
from statistics import mean, median
from E10lru_cache import LRUCache

@Pyro4.expose
class StatsServer:
    def __init__(self):
        self.cache = LRUCache(capacity=3)

    def calculate_mean(self, numbers):
        key = ("mean", tuple(numbers))
        cached = self.cache.get(key)
        if cached is not None:
            print("Returning cached mean")
            return cached
        result = mean(numbers)
        self.cache.put(key, result)
        return result

    def calculate_median(self, numbers):
        key = ("median", tuple(numbers))
        cached = self.cache.get(key)
        if cached is not None:
            print("Returning cached median")
            return cached
        result = median(numbers)
        self.cache.put(key, result)
        return result

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(StatsServer)
ns.register("stats2", uri)  
print("StatsServer is ready.")
daemon.requestLoop()
