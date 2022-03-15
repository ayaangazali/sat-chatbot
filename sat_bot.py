"""SAT chatbot - helps answer and quiz SAT practice questions."""


def main():
    print("SAT bot is starting up.")
    while True:
        choice = input("Pick a mode> ").strip().lower()
        if choice == "/quit":
            print("Bye! Good luck on the SAT.")
            break
        else:
            print("Not sure what that means yet.")


if __name__ == "__main__":
    main()
