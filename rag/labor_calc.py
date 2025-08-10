def calculate_labor_cost(hours: float, rate_per_hour: float) -> float:
    """
    Calculate labor cost based on hours and hourly rate.
    """
    if hours < 0 or rate_per_hour < 0:
        raise ValueError("Hours and hourly rate must be non-negative")
    return round(hours * rate_per_hour, 2)