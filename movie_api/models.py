from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Float
)

from .database import Base


class Movie(Base):
    __tablename__ = "movie_meta"

    id = Column(Integer, primary_key=True, index=True)
    release_date = Column(String)
    budget = Column(Float)
    revenue = Column(Float)

class Genre(Base):
    __tablename__ = "movie_genres"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class MovieGenreLookup(Base):
    __tablename__ = "movie_genre_lookup"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movie_meta.id"))
    genre_id = Column(Integer, ForeignKey("movie_genres.id"))


class ProductionCompany(Base):
    __tablename__ = "production_companies"

    id = Column(Integer, primary_key=True)
    name = Column(String)


class ProductionMovieLookup(Base):
    __tablename__ = "production_movie_lookup"

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movie_meta.id"))
    production_id = Column(Integer, ForeignKey("production_companies.id"))


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer)
    rating = Column(Float)
