"""SAT chatbot - helps answer and quiz SAT practice questions."""

import json
import os

from dotenv import load_dotenv
import openai

QUESTIONS_FILE = "questions.json"


def setup():
    """Load the API key from the environment."""
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("No OPENAI_API_KEY found. Copy .env.example to .env and add your key.")
        return False
    openai.api_key = api_key
    return True


def load_questions(path=QUESTIONS_FILE):
    """Load the SAT question bank from a JSON file."""
    try:
        with open(path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Could not find the question bank at {path}.")
        return []
    except json.JSONDecodeError:
        print(f"The question bank at {path} is not valid JSON.")
        return []


def show_menu():
    print("\n=== SAT Bot ===")
    print("1) Explain mode - paste a question and get a step-by-step explanation")
    print("2) Quiz mode - get quizzed on practice questions")
    print("Type /quit to exit.")


def main():
    if not setup():
        return
    questions = load_questions()
    print(f"SAT bot is ready. Loaded {len(questions)} questions.")
    while True:
        show_menu()
        choice = input("Pick a mode> ").strip().lower()
        if choice == "/quit":
            print("Bye! Good luck on the SAT.")
            break
        elif choice == "1":
            print("(explain mode coming soon)")
        elif choice == "2":
            print("(quiz mode coming soon)")
        else:
            print("Please pick 1, 2, or /quit.")


if __name__ == "__main__":
    main()
