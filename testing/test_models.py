import unittest
import uuid
from models import Scale

class DummyScale(Scale):
    """A concrete scale class intended solely for testing purposes, used to instantiate the abstract Scale class."""
    def generate_id(self):
        random_part = uuid.uuid4().hex[:6].upper()
        self._id = f"{self.model_name.replace(' ', '').upper()}-{random_part}"

class TestScale(unittest.TestCase):
    def setUp(self):
        """Initialize a fresh DummyScale instance before each test method runs."""
        self.scale = DummyScale(model_name="TestScale", category="Test", max_weight_g=1000)

    def test_initial_state(self):
        """Verify that a newly instantiated scale is powered off with zero weight and tare."""
        self.assertFalse(self.scale.is_on)
        self.assertEqual(self.scale.current_weight_g, 0)
        self.assertEqual(self.scale.net_weight, 0)

    def test_power_toggle(self):
        """Check that the power toggle correctly switches the scale's state on and off."""
        self.scale.toggle_power()
        self.assertTrue(self.scale.is_on)
        self.scale.toggle_power()
        self.assertFalse(self.scale.is_on)

    def test_overload_logic(self):
        """Ensure the scale properly reports being overloaded only when powered on and exceeding max weight."""
        self.scale.toggle_power()
        self.scale.current_weight_g = 1500
        self.assertTrue(self.scale.is_overloaded)
        
        # Test: overload have to be false if the scale is turned out
        self.scale.toggle_power()
        self.assertFalse(self.scale.is_overloaded)

    def test_net_weight(self):
        """Validate that the net weight properly subtracts the tare weight from the current weight."""
        self.scale.toggle_power()
        self.scale.current_weight_g = 500
        self.scale.tare_weight_g = 100
        self.assertEqual(self.scale.net_weight, 400)

    def test_generate_id(self):
        """Test the dynamic ID generation logic to ensure correct prefix formatting, length, and randomness."""
        self.scale.generate_id()
        self.assertIsNotNone(self.scale.get_id())
        self.assertIsInstance(self.scale.get_id(), str)
        self.assertTrue(self.scale.get_id().startswith("TESTSCALE-"))
        self.assertEqual(len(self.scale.get_id()), 16)
        self.assertEqual(self.scale.get_id()[-6:].isalnum(), True)

    def test_get_id(self):
        """Verify that the get_id() getter correctly returns the internally stored _id attribute."""
        self.scale.generate_id()
        self.assertEqual(self.scale.get_id(), self.scale._id)

    def test_repr(self):
        """Check the developer-facing string representation (__repr__) for correct formatting."""
        self.scale.toggle_power()
        self.scale.current_weight_g = 500
        self.scale.tare_weight_g = 100
        self.assertEqual(self.scale.__repr__(), "Scale(model=TestScale, weight=500g, on=True)")

    def test_str(self):
        """Check the user-facing string representation (__str__) for correct formatting."""
        self.scale.toggle_power()
        self.scale.current_weight_g = 500
        self.scale.tare_weight_g = 100
        self.assertEqual(self.scale.__str__(), "TestScale [ON]: 500g / 1000g max")

if __name__ == "__main__":
    unittest.main()
