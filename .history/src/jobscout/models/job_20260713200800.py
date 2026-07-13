from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl


class Job(BaseModel):
    """
    Represents a job posting.
    """

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

    skills: list[str] = []