import os
import sys
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash
from app.core.config import settings

def seed() -> None:
    db: Session = SessionLocal()
    admin_email = settings.ADMIN_EMAIL.lower()
    user = db.query(User).filter(User.email == admin_email).first()
    if not user:
        print("Creating admin user...")
        user = User(
            email=admin_email,
            hashed_password=get_password_hash(settings.ADMIN_PASSWORD),
            is_admin=True,
        )
        db.add(user)
        db.commit()
    else:
        print("Admin user already exists.")
    
    # Assuming diagnostic centres and tests could be added here
    db.close()

if __name__ == "__main__":
    seed()
