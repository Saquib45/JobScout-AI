from sqlalchemy import create_engine

DATABASE_URL = (
    "mysql+pymysql://root:9960844980&Ss@localhost:3306/jobscout_db"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
)