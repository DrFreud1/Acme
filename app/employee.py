from collections import defaultdict
from datetime import datetime


class Employee:
    def __init__(self, name: str, shift_data: str):
        self.name = name
        self.shift_data = self.parse_shift(shift_data)
        self.credit = 0

    def __str__(self) -> str:
        return f"Employee: {self.name} Credit: {self.credit}"

    @staticmethod
    def load_shifts(file_path: str) -> list:
        employees = list()
        with open(file_path) as file:
            for line in file.read().splitlines():
                name, shift_data = line.split("=")
                employees.append(Employee(name, shift_data))
        return employees

    @staticmethod
    def parse_shift(shift_data: str) -> defaultdict:
        parsed_shifts = defaultdict(list)
        for record in shift_data.split(","):
            day, shift = record[:2], record[2:]
            start, end = shift.split("-")
            start = datetime.strptime(start, "%H:%M").time()
            end = datetime.strptime(end, "%H:%M").time()
            parsed_shifts[day].append((start, end))
        return parsed_shifts
