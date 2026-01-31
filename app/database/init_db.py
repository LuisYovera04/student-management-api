# app/database/init_db.py
from app.database.db_config import engine, Base
from app.models.student import Student

def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully in 'database.db'!")

if __name__ == "__main__":
    init_db()