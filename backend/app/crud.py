from sqlalchemy.orm import Session
from .models import User, Route
from .schemas import UserCreate


def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if user is None:
        return None

    if user.password != password:
        return None

    return user


def get_routes(db: Session, source: str, destination: str):
    return db.query(Route).filter(
        Route.source == source,
        Route.destination == destination
    ).all()