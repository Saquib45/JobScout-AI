from sqlalchemy import text

from jobscout.database.connection import engine

with engine.connect() as conn:
    result = conn.execute(text("SELECT VERSION()"))

    print(result.fetchone())