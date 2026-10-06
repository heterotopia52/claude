from app.schemas import PythonExplanation
from app.prompts import PYTHON_EXPLANATION_PROMPT
from app.client import ClaudeClient


def main():
    client = ClaudeClient(model="claude-haiku-4-5")
    concept = input("Enter a Python concept: ").strip()

    if not concept:
        print("Please enter a Python concept. ").strip()
        return

    prompt = PYTHON_EXPLANATION_PROMPT.format(concept=concept)

    result = client.ask_structured(
        prompt=prompt,
        output_format=PythonExplanation
    )

    print("\nCONCEPT:")
    print(result.concept)

    print("\nEXPLANATION:")
    print(result.explanation)

    print("\nEXAMPLE:")
    print(result.example)

    print("\nCOMMON MISTAKE:")
    print(result.common_mistake)


if __name__ == "__main__":
    main()
