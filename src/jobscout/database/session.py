from sqlalchemy.orm import sessionmaker

from jobscout.database.connection import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)