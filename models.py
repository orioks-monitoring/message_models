from typing import Literal

from pydantic import BaseModel, PositiveInt, field_validator, ValidationInfo


class BaseMessage(BaseModel):
    type: Literal["mark", "homework", "request", "new", "to_admins"]


class ChangeMessage(BaseMessage):
    type: Literal["mark", "homework", "request", "new"]
    user_telegram_id: PositiveInt


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


class OrioksRequestMessage(BaseModel):
    user_telegram_id: PositiveInt
    event_type: Literal[
        "marks",
        "homeworks",
        "requests-questionnaire",
        "requests-doc",
        "requests-reference",
        "news",
        "news-individual",
    ]
    news_id: int | None = None

    @field_validator('news_id')
    def news_id_must_be_only_if_event_type_is_news_individual(
        cls, v: int, info: ValidationInfo
    ) -> int:
        if info.data.get('event_type') != 'news-individual':
            raise ValueError(
                'news_id must be only if event_type is news-individual'
            )
        return v
