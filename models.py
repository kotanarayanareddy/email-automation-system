from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Recipient(Base):
    __tablename__ = "recipients"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    status = Column(String, default="Pending")  # Pending, Sent, Failed

DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

def create_database():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    create_database()
    print("Database and tables created successfully.")