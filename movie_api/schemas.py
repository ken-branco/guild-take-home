from pydantic import BaseModel


class MovieBase(BaseModel):
    release_date: str
    budget: float = 0
    revenue: float = 0


class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True


class GenreBase(BaseModel):
    name: str = ''


class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True


class ProductionCompanyBase(BaseModel):
    name: str = ''


class ProductionCompany(ProductionCompanyBase):
    id: int

    class Config:
        orm_mode = True


class RatingBase(BaseModel):
    movie_id: int
    rating: float


class Rating(RatingBase):
    movie_id: int
    rating: int

    class Config:
        orm_mode = True


class PopularGenreByYear(BaseModel):
    genre_name: str
    total_revenue: float
    average_rating: float


class ProductionMovieBudgetByYear(BaseModel):
    year: str
    company: str
    budget: float
    revenue: float
