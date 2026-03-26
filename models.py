
# BASE CLASS

class Scale:
        """
        Base class for all electronic scales.
        Contains shared attributes and the core logic.
        """
        def __init__(
                    self,
                    model_name: str,
                    category: str,
                    max_weight_g: int,
                    accuracy_g: float = 10
        ):
              
            # FIXED ATTRIBUTES (Base Model)
            self.model_name = model_name            # Scale model
            self.category = category                # Scale mategory (industry, household, etc.)
            self.max_weight_g = max_weight_g        # The limit until ERR
            self.accuracy_g = accuracy_g            # Accuracy from the load cell
            # ...

            # STATE ATTRIBUTES
            self.is_on: bool = False                # Power On/Off
            self.current_weight_g: int = 0          # Current weight
            self.tare_weight_g: int = 0             # Current Tare Value


        @property
        def is_overloaded(self) -> bool:
            """
            Auto checks if  the current weight exceeds the limit
            """
            return self.current_weight_g > self.max_weight_g
        
        @property
        def net_weight(self) -> int:
            """
            Returns weight minus tare
            """
            return self.current_weight_g - self.tare_weight_g
    
        def __repr__(self) -> str:
            return f"Scale(model={self.model_name}, weight={self.current_weight_g}g, overloaded={self.is_overloaded})"
        
        def __str__(self) -> str:
            status = "ON" if self.is_on else "OFF"
            return f"{self.model_name} [{status}]: {self.current_weight_g}g / {self.max_weight_g}"

    # CHILDREN CLASS

class PostOfficeScale(Scale):
    def __init__(self, category="Industry", max_weight_g=30_000):
        """
        Placeholder!
        """    
        super().__init__(model="Post Office Model", category=category,
                         max_weight_g=max_weight_g, accuracy=10)
        
        self.current_unit: str = "kg"
        self.pc_interface: str = "usb3.0"
        # ...