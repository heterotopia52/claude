from pydantic import BaseModel


class PythonExplanation(BaseModel):
    concept: str
    explanation: str
    example: str
    common_mistake: str
       
