## Movie API

Requires Python 3.10+  

### ERD 
![Movie API ERD](https://github.com/ken-branco/guild-take-home/blob/master/data/movie-api-erd.pdf "Moview API ERD")

The ERD was implemented in an [SQLite3](https://www.sqlite.org/index.html) database.  
THe database used by the API is in /data/movies.db  

An autoincrement Id column was added to the `ratings` table and both lookup tables.  
SQLAlchemy ORM would not load tables without a PK


### How to Install Dependencies
Run this command from the repository root directory.
  
`pip install -r requirements`  
 

### How to Run Tests  

`pytest -vvv`  

### How to Start the API Service
`uvicorn movie_api.main:app --reload`  

### API Assumptions  
Definition of most poplular Genre is the one with most revenue for given year input.  

### How to View API documentation
After starting the service, open your web browser here:  
http://127.0.0.1:8000/docs  

Click on each GET endpoint then click "Try it out" button.
This will present input boxes for endpoint query parameters

