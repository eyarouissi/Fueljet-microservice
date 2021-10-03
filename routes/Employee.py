#from _typeshed import ReadableBuffer
from re import MULTILINE
from fastapi import APIRouter, Body,  Request
from fastapi.encoders import jsonable_encoder
import pymongo
from starlette.routing import request_response 
from database.database import *
from models.Employee import *
from config import settings
from motor.motor_asyncio import AsyncIOMotorClient
import  pymongo
import asyncio
router = APIRouter()


#Returns the roles
@router.get("/get_roles", response_description="roles retrieved")
async def get_roles(company_name: str):

    doc = list ( Projects_collection.find({}, {"Role":1, "_id":0}))
    
    if doc == [] :
     return ErrorResponseModel("An error occured.", 404, " The roles are not found")
    else :
     return ResponseModel("the roles  are : {}  ".format(doc), "Roles retrieved successfully")

#Returns the competencies per role
@router.get("/get_competencies_per_role", response_description="competencies retrieved")
async def get_competencies_per_role(role: str):

    doc = list ( Projects_collection.find({ "Role" : role},{"Competencies":1, "_id":0}))
    
    if doc == [] :
     return ErrorResponseModel("An error occured.", 404, " The top 10 competencies are not found")
    else :
     return ResponseModel("the competencies are : {}  ".format(doc), "Top 10 competencies retrieved successfully")

 
#Returns the competencies per role
@router.get("/get_competencies", response_description="competencies retrieved")
async def get_competencies(company_name: str):

    doc = list ( Projects_collection.find({},{"Competencies":1, "_id":0}))
    
    if doc == [] :
     return ErrorResponseModel("An error occured.", 404, " The competencies are not found")
    else :
     return ResponseModel("the competencies are : {}  ".format(doc), "All the competencies retrieved successfully")