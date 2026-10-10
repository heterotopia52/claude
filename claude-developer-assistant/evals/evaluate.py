import json
from pathlib import Path
from app.client import ClaudeClient
from app.prompts import PYTHON_EXPLANATION_PROMPT
from app.schemas import PythonExplanation

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATASET_PATH = PROJECT_ROOT / "evals" / "dataset01.json"


def load_dataset():
    with DATASET_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def score_answer(answer: str, expected_topics: list[str]) -> int:
    answer_lower = answer.lower()
    matches = 0
    for topic in expected_topics:
        if topic.lower() in answer_lower:
            matches += 1
    return matches


def main():
    dataset = load_dataset()
    client = ClaudeClient(model="claude-haiku-4-5")

    total_score = 0
    total_possible_questions = 0

    for entry in dataset:
        prompt = PYTHON_EXPLANATION_PROMPT.format(concept=entry["question"])
        response = client.ask_structured(
            prompt=prompt,
            output_format=PythonExplanation,
        )

        answer = (
            f"{response.concept}\n"
            f"{response.explanation}\n"
            f"{response.example}\n"
            f"{response.common_mistake}\n"
        )

        score = score_answer(answer, entry["expected_topics"])
        total_score += score
        total_possible_questions += len(entry["expected_topics"])

        print(f"\n Case: {entry['id']}")
        print(f"Question: {entry['question']}")
        print(f"Score: {score}/{len(entry['expected_topics'])}\n")

    print("\n======================")
    print("Evaluation Summary")
    print("======================")
    print(f"Total Score: {total_score}/{total_possible_questions}")

    percentage = (total_score / total_possible_questions) * 100 
    print(f"Percentage: {percentage:.1f}%")


if __name__ == "__main__":
    main()    