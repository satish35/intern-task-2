from fastapi import FastAPI, Response, Depends
from fastapi.requests import Request
from router import endpoints
from router.database import schemas,models,database
from sqlalchemy.orm import Session
from datetime import date, datetime, timezone


app = FastAPI(title="Task")
models.Base.metadata.create_all(bind=database.engine)
def get_db():
    db=database.Session()
    try:
        yield db
    finally:
        db.close()

@app.post('/include-plan')
async def plan_include(plan: schemas.PlanFinal, db: Session= Depends(get_db)):
    res= await endpoints.include_plan(plan, db)
    return res

@app.post('/customer-register')
async def customer_register(customer: schemas.CustomerRegister, db: Session= Depends(get_db)):
    res= await endpoints.register(customer, db)
    return res

@app.post('/map-customer-plan')
async def map_plan(customer: schemas.CustomerSubscribe, db: Session= Depends(get_db)):
    res= await endpoints.map_plan(customer, db)
    return res

@app.get('/get-all-plan')
async def get_plan(db: Session= Depends(get_db), skip: int = 0, limit: int = 100 ):
    res= await endpoints.get_plan(db)
    return res

@app.post('/get-customer-plan')
async def get_customer_plan(id: schemas.CustomerRegister, db: Session= Depends(get_db)):
    res= await endpoints.get_customer_plan(id, db)
    return res

