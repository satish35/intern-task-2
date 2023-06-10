from fastapi import APIRouter, Depends, HTTPException
from .database import database, models, schemas
from sqlalchemy.orm import Session
from datetime import date, datetime, timezone

router=APIRouter()
models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db=database.Session()
    try:
        yield db
    finally:
        db.close()


@router.post('/customer-register', tags=['endpoints'])
async def register(id: schemas.CustomerRegister):
    new_customer=models.Customer_plan(customer_id=id)
    res=database.Session().add(new_customer)
    database.Session().commit()
    database.Session().close()
    return res


@router.post('/include-plan', tags=['endpoints'])
async def include_plan(plan: schemas.PlanFinal):
    new_plan=models.Plan(plan_id= plan.plan_id, active= plan.active)
    res=database.Session().add(new_plan)
    database.Session().commit()
    database.Session().close()
    return res


@router.get('/get-all-plans', tags=['endpoints'])
async def get_plan(skip: int = 0, limit: int = 100):
    res=database.Session().query(models.Plan).offset(skip).limit(limit).all()
    database.Session().close()
    return res

    
@router.post('/map-customer-plan', tags=['endpoints'])
async def map_plan(customer: schemas.CustomerSubscribe):
    res=database.Session().query(models.Customer_plan).where(models.Customer_plan.customer_id == customer.customer_id)
    if res is None:
        raise HTTPException('user does not exist')
    else:
        update_plan=res.update({"p_id": customer.plan_id}, {"valid_till": datetime.now(timezone.utc)})
        database.Session().execute(update_plan)
        database.Session().close()
        return update_plan
    
    
@router.post('/get-customer-plan', tags=['endpoints'])
async def get_customer_plan(id: schemas.CustomerRegister):
    res=database.Session().query(models.Customer_plan).filter(models.Customer_plan.customer_id == id.customer_id)
    if res is None:
        raise HTTPException('No such customer')
    else:
        database.Session().close()
        return res
