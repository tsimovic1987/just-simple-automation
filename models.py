
# BASE CLASS

class Models:
    def __init__(self, model: str, category: str, max_weight_g: int=50000, accuracy: int=10): 
        """
        This class contains everything that EVERY electronic scale in the world has in common.

        More coming soon! Placeholder!
        """

        # FIXED ATTRIBUTES (Base Model)

        self.model = model                  # Scale model
        self.category = category            # Scale mategory (industry, household, etc.)
        self.max_weight_g = max_weight_g    # The limit until ERR
        self.accuracy = accuracy            # coming soon!
        # ...

        # FLEXIBLE ATTRIBUTES (Custom Model)

        self.is_on: bool = False
        self.current_weight_0: int = 0
        self.tare_weight_g: int = 0
        self.is_overloaded: bool = False
        # ...

    
    def __str__(self) -> str:
        return f""


    # ...


class PostOfficeScale(Models):
    def __init__(self, category="Industry", max_weight_g=30_000):
        """
        Placeholder!
        """    
        super().__init__(model="Post Office Model", category=category,
                         max_weight_g=max_weight_g, accuracy=10)
        
        self.current_unit: str = "kg"
        self.pc_interface: str = "usb3.0"
        # ...