from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import *
from ..schemas import *
from ..deps import *

router = APIRouter(prefix="/departments", tags=["departments"])

@router.post("", response_model=DepartmentOut, status_code=201)
def create_department(payload: DepartmentCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    dep = Department(department_name=payload.department_name, submitted_by=user.id)
    db.add(dep)
    db.commit()
    db.refresh(dep)
    return dep

@router.get("", response_model=list[DepartmentOut])
def list_departments(db: Session = Depends(get_db)):
    return db.query(Department).all()