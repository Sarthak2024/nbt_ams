import secrets
from fastapi import FastAPI
from sqlalchemy.orm import Session
from .db import Base, engine, SessionLocal
from .models import User
from .security import get_password_hash
from .routers import auth, users, departments, students, courses, attendance

app = FastAPI(title="Attendance Management System")

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

    # Auto-create first admin if no users
    with SessionLocal() as db:  # type: Session
        if db.query(User).count() == 0:
            raw_password = "Admin@123"
            admin = User(
                type="admin",
                full_name="Sarthak Agrawal",
                username="sarthak1",
                email="sarthak92587@gmail.com",
                password=get_password_hash(raw_password),
            )
            db.add(admin)
            db.commit()

# Routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(departments.router)
app.include_router(students.router)
app.include_router(courses.router)
app.include_router(attendance.router)

@app.get("/health")
def health():
    return {"status": "ok"}
