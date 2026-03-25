from collections import Counter

class PartsList:
    def __init__(self, model_obj):
        self.model = model_obj

        self.partslist = Counter({
            "Bolts M5": 2,
            "Nuts": 4,
            # ...
        })