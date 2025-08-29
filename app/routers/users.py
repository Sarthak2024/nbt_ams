from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import *
from ..schemas import *
from ..security import *
from ..deps import *

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserOut, dependencies=[Depends(admin_required)], status_code=201)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter((User.username == payload.username) | (User.email == payload.email)).first():
        raise HTTPException(400, detail="Username or email already exists")
    user = User(
        type=payload.type,
        full_name=payload.full_name,
        username=payload.username,
        email=payload.email,
        password=get_password_hash(payload.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("", response_model=list[UserOut], dependencies=[Depends(admin_required)])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

