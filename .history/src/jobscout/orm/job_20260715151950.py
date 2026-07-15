from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from jobscout.database.base import Base


class JobORM(Base):
    """Represents a job stored in the database."""

    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    company: Mapped[str] = mapped_column(String(100), nullable=False)

    title: Mapped[str] = mapped_column(String(255), nullable=False)

    location: Mapped[str] = mapped_column(String(255), nullable=False)

    url: Mapped[str] = mapped_column(String(1000),
    unique=True,
    nullable=False,
)

    posted_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    description: Mapped[str] = mapped_column(Text, default="")

    employment_type: Mapped[str] = mapped_column(String(100), default="")

    experience: Mapped[str] = mapped_column(String(100), default="")

    salary: Mapped[str] = mapped_column(String(100), default="")

    source: Mapped[str] = mapped_column(String(100), default="")

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )