from sqlalchemy import create_engine

DATABASE_URL = (
    "mysql+pymysql://rooft:9960844980&Ssf@localhost:3306/jobscout_db"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
)