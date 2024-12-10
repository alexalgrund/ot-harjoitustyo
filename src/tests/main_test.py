import unittest
from main import MainGame
import pygame
import sys
import os


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
        self.assertIsNotNone(self.kortti.sounds['beep'])
        self.assertIsNotNone(self.kortti.sounds['crush'])
        self.assertIsNotNone(self.kortti.sounds['wump'])
