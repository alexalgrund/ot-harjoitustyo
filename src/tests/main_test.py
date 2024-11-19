import unittest
import pygame
from main import CutleryHunt

class TestCutleryHunt(unittest.TestCase):

    def setUp(self):
        self.kortti = CutleryHunt()

    def test_download_pics(self):
        cutlery_hunt = CutleryHunt()
        self.assertIsNotNone(cutlery_hunt.forkPic)
        self.assertIsNotNone(cutlery_hunt.knifePic)
        self.assertIsNotNone(cutlery_hunt.knightPic)
        self.assertIsNotNone(cutlery_hunt.skeletonPic)
        self.assertIsNotNone(cutlery_hunt.spoonPic)
        self.assertIsNotNone(cutlery_hunt.wallPic)

    def test_download_voices(self):
        self.assertIsNotNone(cutlery_hunt.sounds['beep'])
        self.assertIsNotNone(cutlery_hunt.sounds['crush'])
        self.assertIsNotNone(cutlery_hunt.sounds['wump'])

