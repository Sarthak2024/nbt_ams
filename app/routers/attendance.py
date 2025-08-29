from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import *
from ..schemas import *
from ..deps import *

router = APIRouter(prefix="/attendance", tags=["attendance"])

@router.post("/mark", response_model=AttendanceOut)
def mark_attendance(payload: AttendanceMark, db: Session = Depends(get_db), user=Depends(get_current_user)):
    rec = AttendanceLog(
        student_id=payload.student_id,
        course_id=payload.course_id,
        present=payload.present,
        submitted_by=user.id,
        updated_at=datetime.now(),
    )
    db.add(rec)
    db.commit()
    db.refresh(rec)
    return rec


@router.get("/by-student", response_model=list[AttendanceOut])

def list_by_student(student_id: int = Query(...), db: Session = Depends(get_db)):
    return db.query(AttendanceLog).filter(AttendanceLog.student_id == student_id).order_by(AttendanceLog.updated_at.desc()).all()
