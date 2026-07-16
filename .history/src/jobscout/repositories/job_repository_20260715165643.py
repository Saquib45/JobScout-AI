from sqlalchemy import select
from sqlalchemy.orm import Session

from jobscout.mappers.job_mapper import JobMapper
from jobscout.models.job import Job
from jobscout.orm.job import JobORM


class JobRepository:
    """Repository for Job database operations."""

    def __init__(self, session: Session):
        self.session = session

    def save(self, job: Job) -> Job:
        orm_job = JobMapper.to_orm(job)

        self.session.add(orm_job)
        self.session.commit()
        self.session.refresh(orm_job)

        return JobMapper.from_orm(orm_job)

    def exists(self, url: str) -> bool:
        stmt = select(JobORM).where(JobORM.url == url)

        return (
            self.session.execute(stmt)
            .scalar_one_or_none()
            is not None
        )

    def get_all(self) -> list[Job]:
        stmt = select(JobORM)

        jobs = self.session.scalars(stmt)

        return [
            JobMapper.from_orm(job)
            for job in jobs
        ]

    def count(self) -> int:
        stmt = select(JobORM)

        return len(list(self.session.scalars(stmt)))