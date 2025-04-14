import Pyro4

uri = input("Enter the Pyro URI of the TextAnalyzer: ").strip()
analyzer = Pyro4.Proxy(uri)

def get_text():
    print("\nChoose input method:")
    print("1. Type text manually")
    print("2. Load text from a file")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        return input("Enter your text: ")

    elif choice == "2":
        file_path = input("Enter the file path: ").strip()
        try:
            with open(file_path, "r") as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return ""

    else:
        print("Invalid choice.")
        return ""

while True:
    print("\nChoose an analysis:")
    print("1. Word Count")
    print("2. Most Common Word")
    print("3. Quit")

    option = input("Enter your choice (1-3): ").strip()
    if option == "3":
        print("Goodbye!")
        break

    text = get_text()
    if not text.strip():
        print("No text provided. Try again.")
        continue

    if option == "1":
        print("Word Count:", analyzer.word_count(text))
    elif option == "2":
        print("Most Common Word:", analyzer.most_common_word(text))
    else:
        print("Invalid option.")
