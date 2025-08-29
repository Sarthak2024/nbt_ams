from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import *
from ..schemas import *
from ..deps import *

router = APIRouter(prefix="/courses", tags=["courses"])

@router.post("", response_model=CourseOut, status_code=201)
def create_course(payload: CourseCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    cr = Course(
        course_name=payload.course_name,
        department_id=payload.department_id,
        semester=payload.semester,
        class_name=payload.class_name,
        lecture_hours=payload.lecture_hours,
        submitted_by=user.id,
    )
    db.add(cr)
    db.commit()
    db.refresh(cr)
    return cr

@router.get("", response_model=list[CourseOut])
def list_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()
