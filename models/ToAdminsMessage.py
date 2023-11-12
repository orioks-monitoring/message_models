from typing import Literal

from models.BaseMessage import BaseMessage


class ToAdminsMessage(BaseMessage):
    type: Literal["to_admins"] = "to_admins"
    message: str
