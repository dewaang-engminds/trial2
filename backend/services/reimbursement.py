# backend/services/reimbursement.py

from collections import defaultdict
from datetime import date


def calculate_reimbursements(ride_logs, start_date, end_date):
    """
    Input:
        - ride_logs: list of rides [{emp_id, date, trip_type}]
        - date range
    Output:
        - Dict[emp_id] -> reimbursed_days
    """
    all_days = set()
    current = start_date
    while current <= end_date:
        all_days.add(current)
        current = current.fromordinal(current.toordinal() + 1)

    rides_by_emp = defaultdict(set)
    for ride in ride_logs:
        if start_date <= ride["date"] <= end_date:
            rides_by_emp[ride["emp_id"]].add(ride["date"])

    reimbursed = {}
    for emp_id, ride_days in rides_by_emp.items():
        reimbursed_days = len(all_days - ride_days)
        reimbursed[emp_id] = reimbursed_days

    return reimbursed
