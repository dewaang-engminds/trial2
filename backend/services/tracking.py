# backend/services/tracking.py

import redis
import os
import json

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
r = redis.Redis.from_url(REDIS_URL)

def update_cab_location(cab_id, lat, lng):
    key = f"cab_location:{cab_id}"
    r.set(key, json.dumps({"lat": lat, "lng": lng}))

def get_cab_location(cab_id):
    key = f"cab_location:{cab_id}"
    loc = r.get(key)
    if loc:
        return json.loads(loc)
    return {"lat": None, "lng": None}
