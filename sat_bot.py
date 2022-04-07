"""SAT chatbot - helps answer and quiz SAT practice questions."""

import os

from dotenv import load_dotenv
import openai


def setup():
    """Load the API key from the environment."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("No OPENAI_API_KEY found. Copy .env.example to .env and add your key.")
        return False
    openai.api_key = api_key
    return True


def main():
    if not setup():
        return
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
