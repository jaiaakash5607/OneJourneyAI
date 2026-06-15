from .database import SessionLocal
from .models import Route

db = SessionLocal()

routes = [
    Route(
        source="Coimbatore",
        destination="Chennai",
        mode="Train",
        cost=180,
        time="6h 20m",
        safety=95
    ),
    Route(
        source="Coimbatore",
        destination="Chennai",
        mode="Bus",
        cost=150,
        time="8h",
        safety=80
    ),
    Route(
        source="Coimbatore",
        destination="Chennai",
        mode="Flight",
        cost=3200,
        time="1h",
        safety=98
    )
]

db.add_all(routes)
db.commit()

print("Routes inserted successfully!")