from pymongo.mongo_client import MongoClient
from models.Employee import Employee, ErrorResponseModel, ResponseModel
import motor.motor_asyncio
from bson import ObjectId
from pydantic.networks import EmailStr
import ssl
import pymongo 
from models import  * 


client = pymongo.MongoClient('mongodb+srv://Rania_Hamdeni:careerboosts2000@cluster0.vfuyb.mongodb.net/test', ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
database = client.CareerBoosts

Projects_collection = database.get_collection('Project')





   
   









