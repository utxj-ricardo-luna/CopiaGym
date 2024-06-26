from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class Users(BaseModel):
    id:Optional[int]
    usuario: str
    password: str
    created_at: str
    estatus: bool
    Id_persona: int