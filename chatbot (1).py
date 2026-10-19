import random
from datetime import datetime

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer go to the doctor? It had a virus!",
    "I would tell you a UDP joke, but you might not get it.",
    "Why was the Python programmer always calm? Because he had no exceptions.",
    "There are 10 kinds of people: those who understand binary and those who don't.",
]

HELP_TEXT = """I understand these commands:
  - hello / hi
  - how are you
  - good morning / good afternoon / good evening / good night
  - what is your name / who made you / how old are you
  - what time is it / what is the date
  - tell me a joke
  - flip a coin / roll a dice
  - thanks
  - bye"""


def has(text, *phrases):
    """Return True if any phrase appears in the text as whole words."""
    padded = " " + text + " "
    for phrase in phrases:
        if " " + phrase + " " in padded:
            return True
    return False


def get_response(user_input):
    """Return the bot's reply for what the user typed (rule-based, using if-elif)."""
    # Clean the input: lowercase and keep only letters, digits and spaces
    text = user_input.lower()
    text = "".join(ch for ch in text if ch.isalnum() or ch == " ").strip()

    if text == "":
        return "Please type something."
    elif has(text, "bye", "goodbye", "exit", "quit", "see you"):
        return "Goodbye!"
    elif has(text, "how are you", "how are you doing", "how r u"):
        return "I'm fine, thanks!"
    elif has(text, "hello", "hi", "hey"):
        return "Hi!"
    elif has(text, "good morning"):
        return "Good morning! Hope you have a great day."
    elif has(text, "good afternoon"):
        return "Good afternoon! How is your day going?"
    elif has(text, "good evening"):
        return "Good evening! How was your day?"
    elif has(text, "good night"):
        return "Good night! Sleep well."
    elif has(text, "your name", "who are you"):
        return "I'm Basic ChatBot."
    elif has(text, "who made you", "who created you", "who built you"):
        return "I was written in Python as a beginner project."
    elif has(text, "how old are you", "your age"):
        return "I was just created, so I'm brand new!"
    elif has(text, "time"):
        return "It's " + datetime.now().strftime("%I:%M %p") + "."
    elif has(text, "date", "today", "what day is it"):
        return "Today is " + datetime.now().strftime("%A, %d %B %Y") + "."
    elif has(text, "joke", "funny"):
        return random.choice(JOKES)
    elif has(text, "flip", "coin"):
        return "It's " + random.choice(["heads", "tails"]) + "!"
    elif has(text, "roll", "dice", "die"):
        return "You rolled a " + str(random.randint(1, 6)) + "!"
    elif has(text, "thanks", "thank you", "thank"):
        return "You're welcome!"
    elif has(text, "i love you"):
        return "That's sweet! I'm just a simple bot, but thank you."
    elif has(text, "help", "commands", "what can you do"):
        return HELP_TEXT
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I know."


def main():
    print("Basic ChatBot (type 'help' for commands, 'bye' to exit)")

    chatting = True
    while chatting:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Bot:", reply)

        if reply == "Goodbye!":
            chatting = False


if __name__ == "__main__":
    main()
