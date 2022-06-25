from sqlalchemy.orm import Session
from . import models, schemas


def get_movie(db: Session, movie_id: int):
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

