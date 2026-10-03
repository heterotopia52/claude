import anthropic
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()
app_key = os.getenv("ANTHROPIC_API_KEY")


message = anthropic.Anthropic().messages.create(
    model="claude-haiku-4-5",
    max_tokens=1000,
    messages=[{"role": "user",
               "content": "Πως εμφανίζουμε ´Τι είναι η Python;"}],
)

console = Console()
console.print(Markdown(message.content[0].text))

