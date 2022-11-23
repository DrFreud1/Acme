from datetime import date, datetime, timedelta

from utils.constants import RATES, SHIFT_RANGE, WEEKDAYS


class PaymentManager:
    @classmethod
    def calculate_compensation(cls, day: str, shift: tuple) -> int:
        compensation = 0
        week_period = "weekday" if day in WEEKDAYS else "weekend"
        for shift_name, hours in cls.slice_shift(shift).items():
            compensation += hours * RATES[week_period][shift_name]
        return compensation

    @classmethod
    def update_balance(cls, employee: object) -> None:
        credit = 0
        for day, shifts in employee.shift_data.items():
            for shift in shifts:
                credit += cls.calculate_compensation(day, shift)
        employee.credit += credit

    @classmethod
    def slice_shift(cls, shift: tuple) -> dict:
        hours_per_shift = dict()
        for shift_number, shift_range in SHIFT_RANGE.items():
            lower = datetime.combine(date.min, max(shift[0], shift_range[0]))
            upper = datetime.combine(date.min, min(shift[1], shift_range[1]))
            hours = max(upper - lower, timedelta(0))
            hours_per_shift[shift_number] = int(round(hours.total_seconds() / 3600, 2))
        return hours_per_shift
