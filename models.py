
# BASE CLASS

class Models:
    def __init__(self, model: str, category: str, max_weight_g: int=50000, accuracy: int=10): 
        """
        This class contains everything that EVERY electronic scale in the world has in common.

        More coming soon! Placeholder!
        """

        # FIXED ATTRIBUTES (Base Model)

        self.model = model                      # Scale model
        self.category = category                # Scale mategory (industry, household, etc.)
        self.max_weight_g = max_weight_g        # The limit until ERR
        self.accuracy = accuracy                # Accuracy from the load cell
        # ...

        # FLEXIBLE ATTRIBUTES (Custom Model)
        # just some random Attributes to test

        self.is_on: bool = False                # Power On/Off
        self.current_weight_0: int = 0          # Current weight
        self.tare_weight_g: int = 0             # Current Tare Value
        self.is_overloaded: bool = False        # Is it overloaded or not exception
        
        # just some examples how it could work in the later app
        # just trying to figure out some ideas

    
    def __str__(self) -> str:
        return f""

        # next dounder methods are coming soon! 

# CHILDREN CLASS - The ordered objects

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