# backend/scheduler/run_clustering.py

from sklearn.cluster import KMeans
import numpy as np
from datetime import datetime
from backend.shared.constants import CAB_CAPACITY

# Dummy employee ride requests for clustering
ride_requests = [
    {"name": "Alice", "lat": 28.50, "lng": 77.10},
    {"name": "Bob", "lat": 28.52, "lng": 77.08},
    {"name": "Charlie", "lat": 28.48, "lng": 77.09},
    {"name": "David", "lat": 28.51, "lng": 77.11},
    {"name": "Eva", "lat": 28.49, "lng": 77.07},
    {"name": "Frank", "lat": 28.53, "lng": 77.12},
    {"name": "Gina", "lat": 28.55, "lng": 77.13},
    {"name": "Harry", "lat": 28.47, "lng": 77.06},
]

def run_clustering():
    print(f"[{datetime.now()}] Running clustering...")

    # Extract lat/lng
    coords = np.array([[r["lat"], r["lng"]] for r in ride_requests])
    
    # Determine number of cabs
    num_cabs = max(1, len(ride_requests) // CAB_CAPACITY + (1 if len(ride_requests) % CAB_CAPACITY > 0 else 0))
    print(f"Total riders: {len(ride_requests)} | Cabs needed: {num_cabs}")

    # Cluster addresses using KMeans
    kmeans = KMeans(n_clusters=num_cabs, n_init=10)
    labels = kmeans.fit_predict(coords)

    # Group assignments
    assignments = {}
    for i, label in enumerate(labels):
        assignments.setdefault(label, []).append(ride_requests[i])

    # Output cluster assignments (can later save to DB)
    for cab_id, stops in assignments.items():
        print(f"\nCab {cab_id + 1} assigned to:")
        for stop in stops:
            print(f" - {stop['name']} ({stop['lat']}, {stop['lng']})")

    return assignments

# Run when script is called directly
if __name__ == "__main__":
    run_clustering()
