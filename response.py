from pydantic import BaseModel

class UserRespose(BaseModel):
    id: int
    name: str
    job: str