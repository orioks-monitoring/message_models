from pydantic import BaseModel


class ToAdminsMessage(BaseModel):
    message: str
