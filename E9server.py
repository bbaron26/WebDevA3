import Pyro4
from collections import Counter

@Pyro4.expose
class TextAnalyzer(object):
    def word_count(self, text):
        words = text.split()
        print(f"word_count called: {len(words)} words")
        return len(words)

    def most_common_word(self, text):
        words = text.lower().split()
        counter = Counter(words)
        if not counter:
            return "No words found."
        most_common = counter.most_common(1)[0]
        print(f"most_common_word called: '{most_common[0]}' ({most_common[1]} times)")
        return most_common[0]

daemon = Pyro4.Daemon()
uri = daemon.register(TextAnalyzer)
print("Ready. Object uri =", uri)
daemon.requestLoop()
