from dataclasses import dataclass
from datetime import datetime

@dataclass
class Measurement:
    weight_g: int
    scale_model: str
    timestamp: datetime = datetime.now()

    
    
import csv

class MeasurementLogger:
    def __init__(self, filename: str = "data.csv"):
        self.filename = filename

    def add_entry(self, entry: Measurement):
        with open(self.filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([entry.timestamp, entry.scale_model, entry.weight_g])