from collections import Counter

class PartsList:
    """
    Manages a list of components for a scale model.
    Uses collections.Counter for efficient inventory management.
    """
    def __init__(self):
        self.components = Counter({
            "Bolts M5": 2,
            "Nuts": 4,
        })

    def add_component(self, name: str, count: int = 1):
        """Adds a specified number of components."""
        self.components[name] += count

    def remove_component(self, name: str, count: int = 1):
        """
        Removes a specified number of components.
        The unary '+' operator removes entries with zero or negative counts.
        """
        self.components[name] -= count
        self.components = +self.components


    