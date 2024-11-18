import unittest
from main import CutleryHunt

class TestCutleryHunt(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")
