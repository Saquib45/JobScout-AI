from jobscout.database.session import get_session
from jobscout.models.job import Job
from jobscout.repositories.job_repository import JobRepository


def main() -> None:
    session = get_session()
    repository = JobRepository(session)

    job = Job(
        company="IBM",
        title="Software Engineer",
        location="Bangalore",
        url="https://ibm.com/jobs/demo-001",
        description="Repository test",
        employment_type="Full Time",
        experience="Fresher",
        salary="Not Disclosed",
        source="IBM Careers",
    )

    if repository.exists(str(job.url)):
        print("⚠ Job already exists.")
    else:
        repository.save(job)
        print("✅ Job inserted.")

    print(f"\nTotal Jobs: {repository.count()}\n")

    for item in repository.get_all():
        print(
            item.company,
            item.title,
            item.location,
        )

    session.close()


if __name__ == "__main__":
    main()