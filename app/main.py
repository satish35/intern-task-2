from fastapi import FastAPI, Response
from fastapi.requests import Request
from router import endpoints
from router.database import schemas

app = FastAPI(title="Task")

@app.post('/include-plan')
async def plan_include(plan: schemas.PlanFinal):
    res= await endpoints.include_plan(plan)
    return res

@app.post('/customer-register')
async def customer_register(customer: schemas.CustomerRegister):
    res= await endpoints.register(customer)
    return res

@app.post('/map-customer-plan')
async def map_plan(customer: schemas.CustomerSubscribe):
    res= await endpoints.map_plan(customer)
    return res

@app.get('/get-all-plan')
async def get_plan():
    res= await endpoints.get_plan()
    return res

@app.post('/get-customer-plan')
async def get_customer_plan(id: schemas.CustomerRegister):
    res= await endpoints.get_customer_plan(id)
    return res


app.include_router(endpoints.router)