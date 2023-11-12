from typing import Literal

from pydantic import BaseModel


class BaseMessage(BaseModel):
    type: Literal["mark", "homework", "request", "new", "to_admins"]


class ChangeMessage(BaseMessage):
    type: Literal["mark", "homework", "request", "new"]
    user_telegram_id: int


class MarkChangeMessage(ChangeMessage):
    type: Literal["mark"] = "mark"
    title_text: str
    mark_change_text: str
    current_grade: float | Literal["н"] | Literal["-"]
    max_grade: float
    caption: str
    side_text: str


class HomeworkChangeMessage(ChangeMessage):
    type: Literal["homework"] = "homework"
    message: str


class RequestChangeMessage(ChangeMessage):
    type: Literal["request"] = "request"
    message: str


class NewChangeMessage(ChangeMessage):
    type: Literal["new"] = "new"
    title_text: str
    side_text: str
    url: str
    caption: str


class ToAdminsMessage(BaseMessage):
    type: Literal["to_admins"] = "to_admins"
    message: str
