from pydantic import BaseModel, EmailStr , Field , model_validator, ConfigDict


class registration(BaseModel):
    full_name: str = Field(min_length = 8, max_length = 40)
    pass_word: str = Field(min_length = 8, max_length = 128)
    email: EmailStr
    confirm_password :str 

    #self refers to the current object of a class.
#after means the validator runs after Pydantic validates the fields and creates the model instance.

    @model_validator(mode="after")
    def check_password(self):
      if self.pass_word!=self.confirm_password:
          raise ValueError("Passwords do not match")
      return self


class registration_response(BaseModel):
   ID: int
   FULL_NAME : str
   EMAIL : EmailStr

   model_config = ConfigDict(from_attributes=True)