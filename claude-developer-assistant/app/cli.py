# import anthropic
# from dotenv import load_dotenv
# import os
# from rich.console import Console
# from rich.markdown import Markdown

from app.schemas import PythonExplanation
from app.client import ClaudeClient

# load_dotenv()
# app_key = os.getenv("ANTHROPIC_API_KEY")

# client = anthropic.Anthropic()


def main():
    client = ClaudeClient(
        model="claude-haiku-4-5"
        )
    result = client.ask_structured(
        prompt="Τι είναι οι decorators στην Python;",
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

# load_dotenv()
# app_key = os.getenv("ANTHROPIC_API_KEY")

# client = anthropic.Anthropic()

# response = client.messages.parse(
#     model="claude-haiku-4-5",
#     max_tokens=1000,        
#     messages=[
#         {
#             "role": "user",
#             "content": "Τι είναι οι decorators στην Python;"
#         }
#     ],
#     output_format=PythonExplanation,            
# )   

# # message = anthropic.Anthropic().messages.create(
# #     model="claude-haiku-4-5",
# #     max_tokens=1000,
# #     messages=[{"role": "user",
# #                "content": "Τι είναι οι decorators στην Python;"}],
# #     )

# result = response.parsed_output

# console = Console()

# # console.print(Markdown(message.content[0].text))

# console.print(Markdown(f"""{result.explanation}"""))
