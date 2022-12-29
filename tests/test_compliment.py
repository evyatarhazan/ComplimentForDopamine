import unittest
from ComplimentForDopamine.compliment import ComplimentGenerator


class TestComplimentGenerator(unittest.TestCase):
    def test_generate_compliment(self):
        generator = ComplimentGenerator("Alice")
        compliment = generator.generate_compliment()
        self.assertIn("Alice", compliment)

