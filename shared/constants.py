# cabroute-ai/shared/constants.py

from datetime import time

# Cutoff time for daily ride check-in (6:00 PM)
CHECKIN_CUTOFF_TIME = time(18, 0)

# Cab capacity (can be modified by admin later)
CAB_CAPACITY = 6

# Roles in the system
ROLE_EMPLOYEE = "employee"
ROLE_DRIVER = "driver"
ROLE_ADMIN = "admin"

# Ride time options
RIDE_AM = "AM"
RIDE_PM = "PM"
RIDE_BOTH = "BOTH"

# Google Maps API (optional: use from env)
GOOGLE_MAPS_BASE_URL = "https://maps.googleapis.com/maps/api"

# Clustering constants
DEFAULT_NUM_CLUSTERS = 3  # fallback if dynamic clustering not used
MAX_CLUSTER_DISTANCE_KM = 5  # optional for DBSCAN, etc.

# Redis keys format
REDIS_GPS_PREFIX = "cab_location:"  # e.g., cab_location:CAB_12
