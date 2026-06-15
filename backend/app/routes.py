from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal
from .schemas import UserCreate
from .crud import create_user

from .schemas import UserLogin
from .crud import login_user
from fastapi import HTTPException

from .schemas import UserCreate, UserLogin

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)

@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):
    result = login_user(
        db,
        user.email,
        user.password
    )

    if result is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "message": "Login Successful",
        "user": {
            "id": result.id,
            "name": result.name,
            "email": result.email
        }
    }


from fastapi import Body

@router.post("/find-route")
def find_route(data: dict = Body(...)):
    source = data["source"]
    destination = data["destination"]

    routes = [
        {
            "type": "Fastest",
            "mode": "Metro + Bus",
            "time": "32 min",
            "cost": "₹40"
        },
        {
            "type": "Cheapest",
            "mode": "Bus",
            "time": "48 min",
            "cost": "₹20"
        },
        {
            "type": "Safest",
            "mode": "Metro",
            "time": "36 min",
            "cost": "₹35"
        }
    ]

    return {
        "source": source,
        "destination": destination,
        "routes": routes
    }


from .ai import recommend_routes
from fastapi import Body

@router.post("/find-route")
def find_route(data: dict = Body(...)):

    source = data["source"]
    destination = data["destination"]

    return recommend_routes(source, destination)

from fastapi import Body
from .crud import get_routes

@router.post("/find-route")
def find_route(
    data: dict = Body(...),
    db: Session = Depends(get_db)
):
    source = data["source"]
    destination = data["destination"]

    routes = get_routes(db, source, destination)

    result = []

    for route in routes:
        result.append({
            "mode": route.mode,
            "cost": route.cost,
            "time": route.time,
            "safety": route.safety
        })

    return {
        "source": source,
        "destination": destination,
        "routes": result
    }