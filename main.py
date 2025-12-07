from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Patient(BaseModel):
    id: str
    name: str
    age: int
    gender: str
    city: str

# basic route
@app.get("/")
def view():
    return {"code": 200, "message": "Hello"}


# using path and query parameters
@app.get("/view/{view_id}")
def view_id(view_id: int, search: Optional[str] = None, sort: Optional[str] = "asc"):
    return {"code": 200, "message": f"Hello , {view_id}, {search}, {sort}"}


@app.post("/create")
def create_patient(patient: Patient):
    # only simulating
    return {"code": 200, "message": patient}


@app.put("/edit/{patient_id}")
def update_patient():
    # perform DB operation
    return JSONResponse(status_code=200, content={"message": "Patient updated successfully"})


@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    # delete from DB
    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"})

