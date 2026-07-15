from sqlalchemy.orm import Session, sessionmaker

from jobscout.database.connection import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def get_session() -> Session:
    """Create and return a new database session."""
    return SessionLocal()