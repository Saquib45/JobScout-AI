from sqlalchemy import create_engine

DATABASE_URL = (
    "mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/jobscout_db"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
)