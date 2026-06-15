def recommend_routes(source, destination):

    routes = [
        {
            "title": "⚡ Fastest",
            "mode": "Train",
            "time": "6h 20m",
            "cost": 180,
            "score": 98
        },
        {
            "title": "💰 Cheapest",
            "mode": "Bus",
            "time": "8h",
            "cost": 150,
            "score": 92
        },
        {
            "title": "🛡 Safest",
            "mode": "Metro + Train",
            "time": "6h 40m",
            "cost": 210,
            "score": 95
        }
    ]

    return {
        "source": source,
        "destination": destination,
        "recommendations": routes
    }