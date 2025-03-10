from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import customers as controller
from ..schemas import customers as schema
from ..schemas.customers import CustomerBase
from ..dependencies.database import get_db

router = APIRouter(
    tags=['Customers'],
    prefix="/customers"
)

class CustomerRead(schema.CustomerBase):
    id: int

@router.post("/", response_model=schema.CustomerRead)
def create_customer(request: schema.CustomerCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.CustomerRead])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{customer_id}", response_model=schema.CustomerRead)
def read_one(customer_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, customer_id)

@router.put("/{customer_id}", response_model=schema.CustomerRead)
def update(customer_id: int, request: schema.CustomerUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, customer_id=customer_id)

@router.delete("/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(customer_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, customer_id=customer_id)
