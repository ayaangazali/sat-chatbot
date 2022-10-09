"""SAT chatbot - helps answer and quiz SAT practice questions."""

import json
import os

from dotenv import load_dotenv
import openai

QUESTIONS_FILE = "questions.json"
MODEL = "text-davinci-003"


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


def ask_llm(prompt):
    """Send a prompt to the OpenAI Completion API and return the text."""
    response = openai.Completion.create(
        engine=MODEL,
        prompt=prompt,
        max_tokens=400,
    )
    return response.choices[0].text.strip()


def explain_mode():
    """Let the user paste an SAT question and have the bot explain it."""
    print("\n--- Explain mode ---")
    print("Paste or type an SAT question (with choices if you have them).")
    print("Type /quit to go back to the menu.\n")
    while True:
        question = input("Question> ").strip()
        if question.lower() == "/quit":
            break
        if not question:
            continue
        prompt = (
            "You are an SAT tutor. Explain the following SAT question step by step, "
            "then state the correct answer clearly at the end.\n\n"
            f"{question}\n\nExplanation:"
        )
        answer = ask_llm(prompt)
        if answer:
            print(f"\n{answer}\n")


def ask_one_question(q):
    """Ask a single multiple-choice question and return True if correct."""
    print(f"\n[{q['section']}] {q['question']}")
    for letter in ("A", "B", "C", "D"):
        print(f"  {letter}) {q['choices'][letter]}")
    while True:
        choice = input("Your answer (A-D, or /quit)> ").strip().upper()
        if choice == "/QUIT":
            return None
        if choice in ("A", "B", "C", "D"):
            break
        print("Please enter A, B, C, or D.")
    if choice == q["answer"]:
        print("Correct!")
        return True
    else:
        print(f"Not quite. The correct answer is {q['answer']}.")
        return False


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
            explain_mode()
        elif choice == "2":
            print("(quiz mode coming soon)")
        else:
            print("Please pick 1, 2, or /quit.")


if __name__ == "__main__":
    main()
