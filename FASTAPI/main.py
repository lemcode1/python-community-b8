from fastapi import FastAPI, Query, Path

from models.employee_model import EmployeeModel
from dao.employee_dao import add_employee_dao
from typing import Annotated

app = FastAPI()

# Develop an api to Display/get a wish message --> Hello Everyone, Good morning
# /showmessage
# {"message": "Hello Everyone, Good morning"}
# GET

@app.post("/addEmployee/{empid}")
def add_employee(empid: Annotated[int, Path(gt=1, le=1000)], emp : EmployeeModel, address : Annotated[str | None, Query(max_length=100, min_length=4)] = None): # address : str | None = None
    print("Input data coming from request body")
    add_employee_dao(emp, address)
    print("Insertion successful")
    return {"message" : "Insertion successfull"}

@app.get("/showmessage")
def wish_message():
    return {"wish_message": "Hi Everyone, Good morning"}

@app.get("/showmessage/{user_name}/{other_name}")
def wish_message(user_name : int, other_name= None):
    return {"wish_message": "Hi " +str(user_name)+ ", Good morning"}

@app.get("/wish_message")
def wish_message(user_name, last_name = None):
    return {"wish_message": "Hi " +str(user_name)+ ", Good morning"}

@app.get("/wish_message/{first_name}")
def wish_message(first_name, last_name):
    return {"wish_message": "Hi " +str(first_name) +" "+last_name+ ", Good morning"}