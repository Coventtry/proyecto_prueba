from pydantic import BaseModel
class subject(BaseModel):
    name : str
    name_teacher: str
    year : int