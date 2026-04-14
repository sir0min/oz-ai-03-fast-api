from datetime import datetime
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    job: str
    created_at: datetime
