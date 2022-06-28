## Movie API

Requires Python 3.10+  

### ERD 
![Moive API ERD](../data/movie-api-erd.pdf "Moview API ERD")  
The ERD was implemented in an [SQLite3](https://www.sqlite.org/index.html) database.  
THe database used by the API is in /data/movies.db  


### How to Install Dependencies
Run this command from the repository root directory.
  
`pip install -r requirements`  
 

### How to Run Tests  

`pytest -vvv`  

### How to Start the API Service
`uvicorn movie_api.main:app --reload`  


### How to View API documentation
After starting the service, open your web browser here:  
http://127.0.0.1:8000/docs  

Click on each GET endpoint then click "Try it out" button.
This will present input boxes for endpoint query parameters

