from sqlalchemy.orm import Session
from . import models, schemas


def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()


# def get_production_company_budget_by_year(db: Session, production_id: str, year: str):
#     return db.query(models.ProductionCompany).filter(models.ProductionCompany.id == production_id)

def get_production_company_budget_by_year(db: Session, production_id: str, year: str):
    for movie, production_company in db.query(models.ProductionMovieLookup).\
             join(models.Movie).\
             join(models.ProductionCompany).\
             filter(models.Movie.id == models.ProductionMovieLookup.movie_id).\
             filter(models.ProductionMovieLookup.production_id == models.ProductionCompany.id).\
             filter(models.Movie.release_date.like(f"%{year}-")).\
             filter(models.ProductionCompany.id == production_id).all():

        return year, production_company.id, production_company.name, sum(movie.budget)


