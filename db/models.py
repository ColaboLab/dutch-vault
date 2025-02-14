from sqlalchemy import Column, Integer, String, CheckConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Noun(Base):
    __tablename__ = "nouns"

    id = Column(Integer, primary_key=True, autoincrement=True)
    word = Column(String, unique=True, nullable=False)
    articles = relationship("NounArticle", back_populates="noun", cascade="all, delete-orphan")

class NounArticle(Base):
    __tablename__ = "noun_articles"

    id = Column(Integer, primary_key=True, autoincrement=True)
    noun_id = Column(Integer, ForeignKey("nouns.id"), nullable=False)
    article = Column(String, nullable=False)

    noun = relationship("Noun", back_populates="articles")

    __table_args__ = (CheckConstraint("article IN ('de', 'het')"),)

class Verb(Base):
    __tablename__ = "verbs"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    infinitive = Column(String, unique=True, nullable=False)
    conjugations = relationship("Conjugation", back_populates="verb")

class Conjugation(Base):
    __tablename__ = "conjugations"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    verb_id = Column(Integer, ForeignKey("verbs.id"), nullable=False)
    pronoun = Column(String, nullable=False)
    tense = Column(String, nullable=False)
    conjugation = Column(String, nullable=False)

    verb = relationship("Verb", back_populates="conjugations")
    
    __table_args__ = (
        UniqueConstraint("verb_id", "pronoun", "tense"),  # Prevent duplicates
        CheckConstraint("tense IN ('present', 'simple past', 'future', 'present perfect')")  # Define allowed tenses
    )