from jobscout.database.base import Base
from jobscout.database.connection import engine

# Import ORM models so SQLAlchemy knows about them
from jobscout.orm.job import JobORM


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully.")


if __name__ == "__main__":
    create_tables()