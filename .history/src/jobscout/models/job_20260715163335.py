from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class Job(BaseModel):
    """Represents a job posting."""

    model_config = ConfigDict(
        validate_assignment=True,
        frozen=False,
    )

    company: str
    title: str
    location: str

    url: HttpUrl

    posted_date: Optional[datetime] = None

    description: str = ""

    employment_type: str = ""

    experience: str = ""

    salary: str = ""

    source: str = ""

    skills: list[str] = Field(default_factory=list)