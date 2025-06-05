# helper/timezone_utils.py

from datetime import datetime, timezone
from typing import Any, Dict

def make_naive_datetime(dt: datetime) -> datetime:
    """Convert timezone-aware datetime to naive datetime by removing timezone info."""
    if dt and hasattr(dt, 'tzinfo') and dt.tzinfo:
        return dt.replace(tzinfo=None)
    return dt

def make_aware_datetime(dt: datetime, tz: timezone = timezone.utc) -> datetime:
    """Convert naive datetime to timezone-aware datetime.""" 
    if dt and (not hasattr(dt, 'tzinfo') or dt.tzinfo is None):
        return dt.replace(tzinfo=tz)
    return dt

def sanitize_datetime_fields(data: Dict[str, Any], fields: list = None) -> Dict[str, Any]:
    """Remove timezone info from specified datetime fields in a dictionary."""
    if fields is None:
        fields = ['created_at', 'updated_at']
    
    sanitized_data = data.copy()
    for field in fields:
        if field in sanitized_data and sanitized_data[field]:
            if isinstance(sanitized_data[field], datetime):
                sanitized_data[field] = make_naive_datetime(sanitized_data[field])
    
    return sanitized_data