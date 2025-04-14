import Pyro4
from datetime import datetime

@Pyro4.expose
class ListProcessor(object):
    def log_action(self, client_id, method_name):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Client {client_id} called {method_name}\n"
        with open("server_log.txt", "a") as log_file:
            log_file.write(log_entry)
        print(log_entry.strip()) 

    def reverse_list(self, client_id, lst):
        self.log_action(client_id, "reverse_list")
        return lst[::-1]

    def remove_duplicates(self, client_id, lst):
        self.log_action(client_id, "remove_duplicates")
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

daemon = Pyro4.Daemon()
uri = daemon.register(ListProcessor)
print("Ready. Object uri =", uri)
daemon.requestLoop()
