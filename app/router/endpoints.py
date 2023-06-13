from fastapi import APIRouter, HTTPException
from .database import database, models, schemas
from sqlalchemy.orm import Session
from datetime import date, datetime, timezone


async def register(id: schemas.CustomerRegister, db: Session):
    new_customer=models.Customer_plan(customer_id = id.customer_id)
    db.add(new_customer)
    db.commit()
    return new_customer


async def include_plan(plan: schemas.PlanFinal, db: Session):
    new_plan=models.Plan(plan_id= plan.plan_id, active= plan.active)
    db.add(new_plan)
    db.commit()
    return new_plan


async def get_plan(db: Session, skip: int = 0, limit: int = 100):
    res=db.query(models.Plan).offset(skip).limit(limit).all()
    print(res)
    db.close()
    return res


async def map_plan(customer: schemas.CustomerSubscribe, db: Session):
    res=db.query(models.Customer_plan).where(models.Customer_plan.customer_id == customer.customer_id).first()
    if res is None:
        raise HTTPException('user does not exist')
    else:
        update_plan=db.query(models.Customer_plan).where(models.Customer_plan.customer_id == customer.customer_id).update({"p_id": customer.plan_id}, {"valid_till": datetime.now(timezone.utc)})
        db.execute(update_plan)
        db.commit()
        return update_plan

async def get_customer_plan(id: schemas.CustomerRegister, db: Session):
    res=db.query(models.Customer_plan).filter(models.Customer_plan.customer_id == id.customer_id).first()
    if res is None:
        raise HTTPException('No such customer')
    else:
        db.close()
        return res
    
