import anthropic
from dotenv import load_dotenv
import os
from pydantic import BaseModel

load_dotenv()
app_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic()


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

    def ask_structured(
        self,
        prompt: str,
        output_format: BaseModel,
    ) -> BaseModel:
        response = self.client.messages.parse(
            model=self.model,
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            output_format=output_format,
        )

        return response.parsed_output

