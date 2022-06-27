from .models import (Movie,
                     Rating,
                     Genre,
                     MovieGenreLookup,
                     ProductionCompany,
                     ProductionMovieLookup
                     )
from sqlalchemy import desc
from sqlalchemy.sql.functions import sum
from sqlalchemy.orm import Session


def get_production_company_budget_by_year(db: Session, production_id: str, year: str):
    budget = 0.0
    for movie, _, production_company in db.query(Movie, ProductionMovieLookup, ProductionCompany, ).\
            filter(ProductionMovieLookup.production_id == production_id).\
            filter(ProductionCompany.id == ProductionMovieLookup.production_id).\
            filter(Movie.id == ProductionMovieLookup.movie_id).\
            filter(Movie.release_date.like(f"%{year}-%")).all():
        budget += movie.budget

    company = production_company.name

    return {"year": year, "budget": budget, "company": company}


def get_most_popular_genre_by_year(db: Session, year: str):

    movie_genre = db.query(Genre.name, sum(Movie.revenue)., sum(Rating.rating), MovieGenreLookup).\
        filter(Rating.movie_id == Movie.id).\
        filter(MovieGenreLookup.movie_id == Movie.id).\
        filter(Genre.id == MovieGenreLookup.genre_id). \
        filter(Movie.release_date.like(f"%{year}-%")).\
        group_by(Genre.name).\
        order_by(sum(Movie.revenue, sum(Rating.rating), desc(Movie.revenue, Rating.rating))).first()

    return movie_genre
