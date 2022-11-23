from datetime import time

RATES = {
    "weekday": {"morning_range": 25, "afternoon_range": 15, "evening_range": 20},
    "weekend": {"morning_range": 30, "afternoon_range": 20, "evening_range": 25},
}
WEEKDAYS = ("MO", "TU", "WE", "TH", "FR")
SHIFT_RANGE = {
    "morning_range": (time(hour=0, minute=0, second=1), time(hour=9, minute=0)),
    "afternoon_range": (time(hour=9, minute=0, second=1), time(hour=18, minute=0)),
    "evening_range": (
        time(hour=18, minute=0, second=1),
        time(hour=23, minute=59, second=59),
    ),
}
