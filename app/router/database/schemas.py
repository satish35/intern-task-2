from pydantic import BaseModel, validator
from datetime import datetime, date, timedelta

class Plan(BaseModel):
    plan_id: int

class PlanFinal(Plan):
    active: bool

    class Config:
        orm_mode=True

class CustomerRegister(BaseModel):
    customer_id: str

class CustomerSubscribe(CustomerRegister):
    plan_id: int
    valid_till: date

    @validator('valid_till')
    def date_check(cls, v):
        if v > v+timedelta(days=90):
            raise ValueError('subscription expired')
        return v
    
class CustomerGet(CustomerSubscribe):
    plan_check: PlanFinal
    
    class Config:
        orm_mode=True

