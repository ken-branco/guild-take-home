from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Float,
    # UniqueConstraint,
    # PrimaryKeyConstraint
)
# from sqlalchemy.orm import relationship
from .database import Base


class Movie(Base):
    __tablename__ = "movie_meta"

    id = Column(Integer, primary_key=True, index=True)
    release_date = Column(String)
    budget = Column(Float)
    revenue = Column(Float)

    # movie_genre_lookup = relationship("MovieGenreLookup", back_populates="movies_genre")
    # movie_production_lookup = relationship("ProductionMovieLookup", back_populates="movies_production")


class Genre(Base):
    __tablename__ = "movie_genres"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # genre_lookup = relationship("MovieGenreLookup", back_populates="genres")


class MovieGenreLookup(Base):
    __tablename__ = "movie_genre_lookup"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movie_meta.id"))
    genre_id = Column(Integer, ForeignKey("movie_genres.id"))

    # movies_genre = relationship("Movie", back_populates="movie_genre_lookup")
    # genres = relationship("Genre", back_populates="genre_lookup")


class ProductionCompany(Base):
    __tablename__ = "production_companies"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # production_lookup = relationship("ProductionMovieLookup", back_populates="movies")


class ProductionMovieLookup(Base):
    __tablename__ = "production_movie_lookup"

    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movie_meta.id"))
    production_id = Column(Integer, ForeignKey("production_companies.id"))

    # movies_production = relationship("Movie", back_populates="movie_production_lookup")
    # production = relationship("ProductionCompany", back_populates="production_lookup")


class Rating(Base):
    __tablename__ = "ratings"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer)
    rating = Column(Float)
