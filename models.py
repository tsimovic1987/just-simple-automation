from abc import ABC, abstractmethod
import uuid
from enum import Enum


class DisplayType(Enum):
    """
    Enum class for diplay type in the scale.
    """
    LCD = "Liquid Crystal Display"
    LED = "Light Emitting Diode"
    OLED = "Organic LED"


class InterfaceType(Enum):
    """
    Enum class for interface type in the scale.
    """
    USB = "USB"
    BLUETOOTH_2 = "Bluetooth 2.0"
    BLUETOOTH_3 = "Bluetooth 3.0"
    BLUETOOTH_4 = "Bluetooth 4.0"
    BLUETOOTH_5 = "Bluetooth 5.0"
    WIFI_2_4 = "WiFi 2.4GHz"
    WIFI_5 = "WiFi 5GHz"
    WIFI_6 = "WiFi 6GHz"
    LAN = "LAN"


class UnitType(Enum):
    """
    Enum class for unit type in the scale.
    """
    G = "Gram"
    KG = "Kilogram"
    LB = "Pound"
    OZ = "Ounce"


class Scale(ABC):
    """
    Base class for all electronic scales.
    Contains shared attributes and core measurement logic.
    """
    def __init__(
        self,
        model_name: str,
        category: str,
        max_weight_g: int,
        display_type: DisplayType,
        interface_type: InterfaceType,
        unit_type: UnitType,
        accuracy_g: float = 10,
    ):

        self.model_name = model_name
        self.category = category
        self.max_weight_g = max_weight_g
        self.display_type = display_type
        self.interface_type = interface_type
        self.unit_type = unit_type
        self.accuracy_g = accuracy_g

        self._id: str = None
        self.is_on: bool = False
        self.display_is_on: bool = False
        self.current_weight_g: int = 0
        self.tare_weight_g: int = 0

    @abstractmethod
    def generate_id(self) -> None:
        """Forces subclasses to implement their own dynamic ID generation logic."""
        pass

    def get_id(self) -> str:
        """Returns the internally stored unique identifier for the scale."""
        return self._id

    @property
    def is_overloaded(self) -> bool:
        """Checks if the weight exceeds the safety limit."""
        if not self.is_on:
            return False
        return self.current_weight_g > self.max_weight_g

    @property
    def net_weight(self) -> int:
        """Returns current weight minus tare if the scale is on."""
        if not self.is_on:
            return 0
        return self.current_weight_g - self.tare_weight_g

    def toggle_power(self) -> None:
        """Simple Power-Switch logic."""
        self.is_on = not self.is_on
        if not self.is_on:
            self.current_weight_g = 0
            self.tare_weight_g = 0

    def toggle_display(self) -> None:
        """Simple Display-Switch logic."""
        self.display_is_on = not self.display_is_on    
        
    def display_info(self) -> str:
        """Simple info which display is installed"""
        return(f"Display: {self.display_type.name}")

    def __eq__(self, other) -> bool:
        if not isinstance(other, Scale):
            return False
        return self.get_id() == other.get_id()

    def __repr__(self) -> str:
        return f"Scale(model={self.model_name}, weight={self.current_weight_g}g, on={self.is_on})"

    def __str__(self) -> str:
        status = "ON" if self.is_on else "OFF"
        weight = f"{self.current_weight_g}g" if self.is_on else "---"
        return f"{self.model_name} [{status}]: {weight} / {self.max_weight_g}g max"


class PostOfficeScale(Scale):
    """Specific scale model for post office usage."""
    def __init__(self, category: str = "Industry", max_weight_g: int = 30000):
        super().__init__(
            model_name="Post Office Model",
            category=category,
            max_weight_g=max_weight_g,
            display_type=DisplayType.OLED,
            interface_type=InterfaceType.LAN,
            unit_type=UnitType.KG,
            accuracy_g=10,
        )

        self.generate_id()

    def generate_id(self) -> None:
        """Generates a unique ID specific to Post Office scales (e.g., 'POSTOFFICEMODEL-XXXXXX')."""
        random_number = uuid.uuid4().hex[:6].upper()
        self._id = f"{self.model_name.replace(' ', '').upper()}-{random_number}"


class KitchenScale(Scale):
    """Specific scale model for kitchen usage."""
    def __init__(self, category: str = "Household", max_weight_g: int = 5000):
        super().__init__(
            model_name="Kitchen Scale",
            category=category,
            max_weight_g=max_weight_g,
            display_type=DisplayType.LED,
            interface_type=InterfaceType.USB,
            unit_type=UnitType.G,
            accuracy_g=1
        )

        self.generate_id()

    def generate_id(self) -> None:
        """Generates a unique ID specific to Kitchen scales (e.g., 'KITCHENSCALE-XXXXXX')."""
        random_number = uuid.uuid4().hex[:6].upper()
        self._id = f"{self.model_name.replace(' ', '').upper()}-{random_number}"