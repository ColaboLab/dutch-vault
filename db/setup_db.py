from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

engine = create_engine("sqlite:///db/dutch_vault.db")
SessionLocal = sessionmaker(bind = engine)

if __name__ == "__main__":
    Base.metadata.create_all(engine)