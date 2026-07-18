# Airline Consultation CRUD in FastAPI

This is a project to understand how HTTP Methods and CRUD works

<ul>
<li>GET: Shows stored data</li>
<li>POST: Adds data</li>
<li>PUT: Updates data</li>
<li>DELETE: Deletes data</li>
</ul>

How to use:
1) Copy the api.py code in your ide and run:
    python -m uvicorn api:app --reload
or  py -m uvicorn api:app --reload

Remember to install fastapi via pip in your terminal. 
python -m pip install "fastapi[all]"
or py -m pip install "fastapi[all]"

After the "Application startup complete." appears, open http://127.0.0.1:8000/docs

2) Try using every method listed above to view, create, update and delete.
    You can search by it's id number or company name. Feel free to edit in the way you like! Enjoy!

PRE-STORED DATA: (The numbers indicate airline's ID). Use for GET and DELETE

```python
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
```

Example for PUT
Airline ID: 2
```python
2: {
    "company": "LATAM",
    "main_hub": "São Paulo",
    "main_fleet": "Airbus A320",
    "year_founded": 2012,
},
```

Example for POST: 
Airline ID: 4
```python
4: {
    "company": "EL AL",
    "main_hub": "Tel Aviv",
    "main_fleet": "787 Dreamliner",
    "year_founded": 1948,
},
```
