from app.client import ClaudeClient
from app.schemas import PythonExplanation


def test_python_explanation():
    client = ClaudeClient(model="claude-haiku-4-5")
    prompt = "Τι είναι οι decorators στην Python;"
    result = client.ask_with_schema(prompt, output_format=PythonExplanation)

    assert isinstance(result, PythonExplanation)
    assert result.concept 
    assert result.explanation
    assert result.example
    assert result.common_mistakes
    
    

