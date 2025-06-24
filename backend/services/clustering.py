# backend/services/clustering.py

from sklearn.cluster import KMeans
import numpy as np
from backend.shared.constants import CAB_CAPACITY


def cluster_addresses(riders):
    """
    Input: List of dicts with lat/lng
    Output: Dict[cab_id] -> list of riders
    """
    if not riders:
        return {}

    coords = np.array([[r["lat"], r["lng"]] for r in riders])
    num_clusters = max(1, len(riders) // CAB_CAPACITY + (1 if len(riders) % CAB_CAPACITY > 0 else 0))

    kmeans = KMeans(n_clusters=num_clusters, n_init=10)
    labels = kmeans.fit_predict(coords)

    assignments = {}
    for idx, label in enumerate(labels):
        assignments.setdefault(label + 1, []).append(riders[idx])  # cab_id = label + 1

    return assignments
