
from fastapi import APIRouter,status, Depends
from schemas.registration import registration  ,registration_response
from services.registration_service import user_register_service
from sqlalchemy.orm import Session
from database.connection import get_db


 
 

router = APIRouter(
    prefix = "/api/auth",
    tags = ["Registration"]
)

#data is a parameter that receives the registration information sent by the frontend.

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=registration_response,)
def user_register(data : registration,
                   db: Session = Depends(get_db)
                  ):
      
      
      
 return user_register_service(data, db)


 
     




