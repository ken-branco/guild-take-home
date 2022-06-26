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


@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@app.get("/production/budget/", response_model=schemas.ProductionMovieBudgetByYear)
def get_production_budget_by_year(production_id: str, year: str, db: Session = Depends(get_db)):
    production_company_budget_for_year = \
        crud.get_production_company_budget_by_year(db, production_id=production_id, year=year)
    if production_company_budget_for_year is None:
        raise HTTPException(status_code=404,
                            detail=f"Production company with id: {production_id} "
                                   f"had no budget for year:{year}")
    return production_company_budget_for_year

