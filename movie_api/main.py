from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/production_company/financials/", response_model=schemas.ProductionMovieBudgetByYear)
def get_production_budget_revenue_by_year(production_id: str, year: str, db: Session = Depends(get_db)):
    production_company_data = \
        crud.get_production_company_budget_revenue_by_year(db, production_id=production_id, year=year)
    if production_company_data is None:
        raise HTTPException(status_code=404,
                            detail=f"Production company with id: {production_id} "
                                   f"had no budget for year:{year}")
    return production_company_data


@app.get("/genre/most_popular/", response_model=schemas.PopularGenreByYear)
def get_most_popular_genre_by_year(year: str, db: Session = Depends(get_db)):
    genre_data = crud.get_most_popular_genre_by_year(db, year=year)
    if genre_data is None:
        raise HTTPException(status_code=404,
                            detail=f"No popular movie genres for year: {year}")
    return genre_data
