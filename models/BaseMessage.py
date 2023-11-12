from typing import Literal

from pydantic import BaseModel


class BaseMessage(BaseModel):
    type: Literal["mark", "homework", "request", "new", "to_admins"]
