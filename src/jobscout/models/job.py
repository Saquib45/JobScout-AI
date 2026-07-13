from pydantic import BaseModel
from datetime import datetime


class Job(BaseModel):
    company: str
    title: str
    location: str
    url: str

    posted_date: datetime | None = None

    description: str = ""

    source: str = ""

    salary: str = ""

    experience: str = ""