from pydantic import BaseModel,Field
from typing import List
from validations.choice import Choice
    
class Question(BaseModel):
    question_text : str
    choices : List[Choice]