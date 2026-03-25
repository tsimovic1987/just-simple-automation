from collections import Counter

class PartsList:
    def __init__(self, model_obj):
        self.model = model_obj

        self.components = Counter({
            "Bolts M5": 2,
            "Nuts": 4,
            # ...
        })

    def add_component(self, name: str, number: int=1):
        self.components[name] += number

    def del_components(self, name: str, number:int=1):
        self.components[name] -= number

        self.components = +self.components

    