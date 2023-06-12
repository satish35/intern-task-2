from .database import Base
from sqlalchemy import Column,BOOLEAN, INTEGER, ForeignKey, DATE, String
from sqlalchemy.orm import relationship

class Plan(Base):
    __tablename__ = "plan"

    plan_id=Column(INTEGER, nullable=False, index=True, primary_key=True)
    active=Column(BOOLEAN, nullable=False)

class Customer_plan(Base):
    __tablename__ = "customer"

    customer_id = customer_id= Column(String, nullable=False, index=True, primary_key=True)
    p_id= Column(INTEGER, ForeignKey('plan.plan_id', ondelete="CASCADE"))
    valid_till = Column(DATE)

    plan_check=relationship('Plan')