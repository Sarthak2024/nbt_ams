from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import *
from ..schemas import *
from ..deps import *

router = APIRRouter = APIRouter(prefix="/students", tags=["students"])

@router.post("", response_model=StudentOut, status_code=201)
def create_student(payload: StudentCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    st = Student(full_name=payload.full_name, department_id=payload.department_id, class_name=payload.class_name, submitted_by=user.id)
    db.add(st)
    db.commit()
    db.refresh(st)
    return st

@router.get("", response_model=list[StudentOut])
def list_students(db: Session = Depends(get_db)):
    return db.query(Student).all()
