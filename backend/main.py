#four things
#Routes
#Configuration
#Middleware
#Database setup
#main.py connects components
#it is a entry point
#create and configure FastAPI application


 
from fastapi import FastAPI, APIRouter
 
from routes.registration import  router
from fastapi.middleware.cors import CORSMiddleware

# middleware is software that processes requests and responses.
# CORS means Cross-Origin Resource Sharing.
# CORSMiddleware is provided by FastAPI through Starlette.


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


app.add_middleware(
     CORSMiddleware,
    allow_origins =["http://127.0.0.1:5500",
                      "http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

# Parameter	Purpose
# allow_origins	Specifies which frontend origins are allowed
# allow_credentials	Allows credentials such as cookies
# allow_methods	Allows HTTP methods such as GET, POST, PUT, DELETE
# allow_headers	Allows request headers







app.include_router(router)






