from typing import Literal

from pydantic import BaseModel


class ChangeMessage(BaseModel):
    type: Literal["mark", "homework", "request"]
    user_telegram_id: int


class MarkChangeMessage(ChangeMessage):
    type: Literal["mark"]
    title_text: str
    mark_change_text: str
    current_grade: float
    max_grade: float
    caption: str
    side_text: str


class HomeworkChangeMessage(ChangeMessage):
    type: Literal["homework"]
    message: str


class RequestChangeMessage(ChangeMessage):
    type: Literal["request"]
    message: str


class NewChangeMessage(ChangeMessage):
    type: Literal["new"]
    title_text: str
    side_text: str
    url: str
    caption: str
