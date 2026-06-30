from pydantic import BaseModel

class UtenteAuth(BaseModel):
    username: str
    password: str