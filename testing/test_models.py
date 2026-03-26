import unittest
from models import Scale

class TestScale(unittest.TestCase):
    def setUp(self):
        self.scale = Scale(model_name="TestScale", category="Test", max_weight_g=1000)

    def test_initial_state(self):
        self.assertFalse(self.scale.is_on)
        self.assertEqual(self.scale.current_weight_g, 0)
        self.assertEqual(self.scale.net_weight, 0)

    def test_power_toggle(self):
        self.scale.toggle_power()
        self.assertTrue(self.scale.is_on)
        self.scale.toggle_power()
        self.assertFalse(self.scale.is_on)

    def test_overload_logic(self):
        self.scale.toggle_power()
        self.scale.current_weight_g = 1500
        self.assertTrue(self.scale.is_overloaded)
        
        # Test: overload have to be false if the scale is turned out
        self.scale.toggle_power()
        self.assertFalse(self.scale.is_overloaded)

    def test_net_weight(self):
        self.scale.toggle_power()
        self.scale.current_weight_g = 500
        self.scale.tare_weight_g = 100
        self.assertEqual(self.scale.net_weight, 400)

if __name__ == "__main__":
    unittest.main()
