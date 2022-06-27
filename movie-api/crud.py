from .models import Movie, ProductionCompany, ProductionMovieLookup
from sqlalchemy.orm import Session



def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()


# def get_production_company_budget_by_year(db: Session, production_id: str, year: str):
#     return db.query(models.ProductionCompany).filter(models.ProductionCompany.id == production_id)

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


