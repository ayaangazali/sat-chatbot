# SAT Bot

A little command-line chatbot for SAT practice. It can explain SAT questions
step by step, and it can quiz you on a small bank of practice questions and
track your score. Explanations are powered by the OpenAI API
(`text-davinci-003`).

## Setup

1. Install the dependencies:

   ```
   pip install -r requirements.txt
   ```

2. Copy the example env file and add your OpenAI API key:

   ```
   cp .env.example .env
   ```

   Then edit `.env` and set:

   ```
   OPENAI_API_KEY=sk-...
   ```

## Usage

Run the bot:

```
python sat_bot.py
```

You'll get a menu with two modes:

- **Explain mode** - paste or type an SAT question (choices included if you
  have them) and the bot explains the answer step by step.
- **Quiz mode** - the bot asks you a few multiple-choice questions from
  `questions.json`, checks your answers, and reports your score. If you miss
  one, it can explain it for you.

Type `/quit` at any prompt to back out of a mode or exit the program.

## Files

- `sat_bot.py` - the CLI app.
- `questions.json` - the practice question bank (Math + Reading/Writing).
- `requirements.txt` - Python dependencies.
- `.env.example` - template for your API key.
