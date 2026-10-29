#four things
#Routes
#Configuration
#Middleware
#Database setup
#main.py connects components
#it is a entry point
#create and configure FastAPI application


 
from fastapi import FastAPI
from fastapi import APIRouter

 
#app
#This is a Python variable that holds the FastAPI application instance. We use app to register endpoints and configure the application.


app =FastAPI(
     title = "Login and Registration  API",
    description ="Backend API for User Registration and Authentication",
    version = "1.0.0"
     )


#there are two related methods you might be seeing:
#- app.include_router() — connects a router to the main FastAPI application.
#- router.include_router() — connects one router to another router.

#main.py
# └── app
#      └── auth_router
#          ├── registration_router
#          └── login_router"


#When we use a router, we still use app, but we define the endpoints using router instead of app in that separate file.

router = APIRouter(
    prefix = "/api/auth",
    tags = ["Registration"]
)


@router.post("/register")
def register_user():
    return{"message" : "Success"}






