Airline Consultation in FastAPI

This is a project to understand how HTTP Methods and CRUD works

GET: Shows stored data
POST: Adds data
PUT: Updates data
DELETE: Deletes date

How to use:
1) Download this repository, open your ide and run:
    python -m uvicorn api:app --reload
or  py -m uvicorn api:app --reload

After the "Application startup complete." appears, open http://127.0.0.1:8000/docs

2) Try using every method listed above to view, create, update and delete.
    You can search by it's id number or company name. Feel free to edit in the way you like! Enjoy!

PRE-STORED DATA: 
'''
     1: {
        "company": "GOL",
        "main_hub": "Sao Paulo",
        "main_fleet": "Boeing 737",
        "year_founded": 2001,
    },

    2: {
        "company": "LATAM",
        "main_hub": "Santiago",
        "main_fleet": "Airbus A320",
        "year_founded": 2012,
    },

    3: {
        "company": "Iberia",
        "main_hub": "Madrid",
        "main_fleet": "Airbus A350-900",
        "year_founded": 1927,
    }
}

 '''
