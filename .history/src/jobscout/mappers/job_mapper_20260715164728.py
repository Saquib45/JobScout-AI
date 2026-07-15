from jobscout.models.job import Job
from jobscout.orm.job import JobORM


class JobMapper:
    """Convert between Job and JobORM."""

    @staticmethod
    def to_orm(job: Job) -> JobORM:
        return JobORM(
            company=job.company,
            title=job.title,
            location=job.location,
            url=str(job.url),
            posted_date=job.posted_date,
            description=job.description,
            employment_type=job.employment_type,
            experience=job.experience,
            salary=job.salary,
            source=job.source,
        )

    @staticmethod
    def from_orm(job: JobORM) -> Job:
        return Job(
            company=job.company,
            title=job.title,
            location=job.location,
            url=job.url,
            posted_date=job.posted_date,
            description=job.description,
            employment_type=job.employment_type,
            experience=job.experience,
            salary=job.salary,
            source=job.source,
        )