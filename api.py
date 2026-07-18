from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

airlines = {
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

class Airline(BaseModel):
    company: str
    main_hub: str
    main_fleet: str
    year_founded: int

class UpdateAirline(BaseModel):
    company: Optional[str] = None
    main_hub: Optional[str] = None
    main_fleet: Optional[str] = None
    year_founded: Optional[int] = None

@app.get("/get-airline/{airline_id}")
def get_airline(airline_id: int = Path(description="Airline ID", gt=0, lt=100)):
    return airlines[airline_id]

@app.get("/get-by-company/{airline_company}")
def get_airline(airline_company: str = Path(description="Airline company")):
    for id in airlines:
        if airlines[id]["company"] == airline_company:
            return airlines[id]
    return {"Error": "Airline not found"}

@app.post("/add-airline/{airline_id}")
def add_airline(airline_id: int, airline: Airline):
    if airline_id in airlines:
        return {"Error": "Airline  exists"}
    airlines[airline_id] = airline
    return airlines[airline_id]

@app.put("/update-airline/{airline_id}")
def update_airline(airline_id: int, airline: UpdateAirline):
    if airline_id not in airlines:
        return {"Error": "Airline does not exist"}
    
    if airline.company != None:
        airlines[airline_id]["company"] = airline.company    
    if airline.main_hub != None:
        airlines[airline_id]["main_hub"] = airline.main_hub    
    if airline.main_fleet != None:
        airlines[airline_id]["main_fleet"] = airline.main_fleet    
    if airline.year_founded != None:
        airlines[airline_id]["year_founded"] = airline.year_founded    

    return airlines[airline_id]

@app.delete("/delete-airline/{airline_id}")
def delete_airline(airline_id: int):
    if airline_id not in airlines:
        return {"Error": "Airline does not exist"}
    del airlines[airline_id]
    return {"Message": "Airline deleted successfully"}