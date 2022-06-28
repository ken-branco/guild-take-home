from fastapi.testclient import TestClient

from movie_api.main import app

client = TestClient(app)


def test_production_financials_existing_company():
    response = client.get("/production_company/financials/?production_id=1&year=1986")
    assert response.status_code == 200
    assert response.json() == {
        "year": "1986",
        "company": "Lucasfilm",
        "budget": 62000000,
        "revenue": 50692691
    }


def test_production_financials_non_existent_company():
    response = client.get("/production_company/financials/?production_id=99999&year=1986")
    assert response.status_code == 200
    assert response.json() == {
        "year": "1986",
        "company": "NOT FOUND",
        "budget": 0,
        "revenue": 0
    }


def test_most_popular_genre_by_year_valid_year():
    response = client.get("/genre/most_popular/?year=1986")
    assert response.status_code == 200
    assert response.json() == {
        "genre_name": "Adventure",
        "total_revenue": 6147610010,
        "average_rating": 3.19
    }


def test_most_popular_genre_by_year_invalid_year():
    response = client.get("/genre/most_popular/?year=9999")
    assert response.status_code == 200
    assert response.json() == {
        "genre_name": "NOT FOUND",
        "total_revenue": 0,
        "average_rating": 0
    }
