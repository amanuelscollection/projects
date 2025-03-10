from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import payment_info as controller
from ..schemas import payment_info as schema
from ..dependencies.database import get_db

router = APIRouter(
    tags=['PaymentInfo'],
    prefix="/payment-info"
)

@router.post("/", response_model=schema.PaymentInfo)
def create_payment_info(request: schema.PaymentInfoCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.PaymentInfo])
def read_all_payment_info(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.PaymentInfo)
def read_one_payment_info(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.PaymentInfo)
def update_payment_info(order_id: int, request: schema.PaymentInfoUpdate, db: Session = Depends(get_db)):
    return controller.update_payment_info(db=db, request=request, order_id=order_id)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_payment_info(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
