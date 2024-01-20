from pydantic import BaseModel,Field
from typing import List

class Choice(BaseModel):
    choice_text : str
    is_correct : bool