import sys
import os

# Fix import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from email_generator.email_generator import EmailGenerator


def main():
    print("\n--- Email Generation Assistant ---\n")

    # Take user input
    intent = input("Enter the intent of the email: ")

    print("\nEnter key facts (one per line, type 'done' when finished):")
    key_facts = []
    while True:
        fact = input("- ")
        if fact.lower() == "done":
            break
        key_facts.append(fact)

    tone = input("\nEnter the desired tone (e.g., formal, casual, urgent): ")

    print("\nGenerating emails...\n")

    try:
        # Model A
        generator_a = EmailGenerator("llama-3.1-8b-instant")

        # Model B
        generator_b = EmailGenerator("openai/gpt-oss-120b")

        email_a = generator_a.generate_email(intent, key_facts, tone)
        email_b = generator_b.generate_email(intent, key_facts, tone)

        print("\n--- Model A (Fast) ---\n")
        print(email_a)

        print("\n--- Model B (High Quality) ---\n")
        print(email_b)

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()