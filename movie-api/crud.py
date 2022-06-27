from .models import (Movie,
                     Rating,
                     Genre,
                     MovieGenreLookup,
                     ProductionCompany,
                     ProductionMovieLookup
                     )
from sqlalchemy import desc
from sqlalchemy.sql.functions import sum, count
from sqlalchemy.orm import Session


def get_production_company_budget_revenue_by_year(db: Session, production_id: str, year: str):
    budget = 0.0
    revenue = 0.0
    production_company = ''
    for movie, _, production_company in db.query(Movie, ProductionMovieLookup, ProductionCompany, ).\
            filter(ProductionMovieLookup.production_id == production_id).\
            filter(ProductionCompany.id == ProductionMovieLookup.production_id).\
            filter(Movie.id == ProductionMovieLookup.movie_id).\
            filter(Movie.release_date.like(f"%{year}-%")).all():
        budget += movie.budget
        revenue += movie.revenue

    company = production_company.name

    return {"year": year, "company": company, "budget": budget, "revenue": revenue}


def get_most_popular_genre_by_year(db: Session, year: str):
    genre_data = \
        db.query(Genre.name, sum(Movie.revenue), sum(Rating.rating), count(Rating.rating), MovieGenreLookup).\
        filter(Rating.movie_id == Movie.id).\
        filter(MovieGenreLookup.movie_id == Movie.id).\
        filter(Genre.id == MovieGenreLookup.genre_id). \
        filter(Movie.release_date.like(f"%{year}-%")).\
        group_by(Genre.name).\
        order_by(desc(sum(Movie.revenue)), desc(sum(Rating.rating))).first()
    genre_name, total_revenue, total_ratings, rating_count, _ = genre_data
    average_rating = total_ratings / rating_count
    return {
        "genre_name": genre_name,
        "total_revenue": total_revenue,
        "average_rating": round(average_rating, 2)
    }
