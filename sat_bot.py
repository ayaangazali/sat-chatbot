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


def main():
    if not setup():
        return
    questions = load_questions()
    print(f"SAT bot is ready. Loaded {len(questions)} questions.")
    while True:
        choice = input("Pick a mode> ").strip().lower()
        if choice == "/quit":
            print("Bye! Good luck on the SAT.")
            break
        else:
            print("Not sure what that means yet.")


if __name__ == "__main__":
    main()
