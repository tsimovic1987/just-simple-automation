import csv
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Measurement:
    scale_id: str
    scale_model: str
    weight_g: int
    is_overloaded: bool
    timestamp: datetime = field(default_factory=datetime.now, compare=False)


class MeasurementLogger:
    def __init__(self, filename: str = "data.csv"):
        self.filename = filename

    def add_entry(self, entry: Measurement):
        with open(self.filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([entry.timestamp, entry.scale_id, entry.scale_model, entry.weight_g, entry.is_overloaded])