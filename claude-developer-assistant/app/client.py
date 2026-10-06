import anthropic
from pydantic import BaseModel


class ClaudeClient:
    def __init__(self, model: str):
        self.client = anthropic.Anthropic()
        self.model = model

    def ask(self, prompt: str) -> str:
        response = self.client.messages.create(
            model=self.model,
            max_tokens=1000,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.content[0].text


class ClaudeRequest(BaseModel):
    summary: str
    question: str
    issues: list[str]
    suggestions: list[str]
    tests: list[str]
