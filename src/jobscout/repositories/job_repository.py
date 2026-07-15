from sqlalchemy import select
from sqlalchemy.orm import Session

from jobscout.orm.job import JobORM


class JobRepository:
    """Repository for Job database operations."""

    def __init__(self, session: Session):
        self.session = session

    def save(self, job: JobORM) -> JobORM:
        """Save a new job."""
        self.session.add(job)
        self.session.commit()
        self.session.refresh(job)
        return job

    def exists(self, url: str) -> bool:
        """Return True if the job URL already exists."""
        stmt = select(JobORM).where(JobORM.url == url)
        return self.session.execute(stmt).scalar_one_or_none() is not None

    def get_all(self) -> list[JobORM]:
        """Return all jobs."""
        stmt = select(JobORM)
        return list(self.session.scalars(stmt))

    def count(self) -> int:
        """Return total number of jobs."""
        return len(self.get_all())