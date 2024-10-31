from enum import Enum
from pydantic import BaseModel, Field, constr


class ContactCategory(str, Enum):
    FAMILY = "family"
    FRIEND = "friend"
    OTHER = "other"


class Contact(BaseModel):
    first_name: constr(strip_whitespace=True, min_length=1) = Field(...)  # type: ignore
    last_name: str | None = ""
    category: ContactCategory | None = ContactCategory.OTHER

    @property
    def name(self) -> str:
        result = self.first_name
        if self.last_name:
            result += " "  + self.last_name
        return result
