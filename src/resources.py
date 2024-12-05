import pygame
import os

class Resources:

    def __init__(self):
        self.images_path = os.path.join(os.path.dirname(__file__), "images")
        self.sounds_path = os.path.join(os.path.dirname(__file__), "sounds")

        #Download pictures
        self.images = {
            "fork": pygame.image.load(os.path.join(self.images_path, "fork.png")),
            "knife": pygame.image.load(os.path.join(self.images_path, "knife.png")),
            "knight": pygame.image.load(os.path.join(self.images_path, "knight.png")),
            "skeleton": pygame.image.load(os.path.join(self.images_path, "skeleton.png")),
            "spoon": pygame.image.load(os.path.join(self.images_path, "spoon.png")),
            "wall": pygame.image.load(os.path.join(self.images_path, "wall.png")),
        }

        #Download voices
        sounds_path = os.path.join(os.path.dirname(__file__), "sounds")
        self.sounds = {
            "beep": pygame.mixer.Sound(os.path.join(sounds_path, "beep.wav")),
            "crush": pygame.mixer.Sound(os.path.join(sounds_path, "crush.wav")),
            "wump": pygame.mixer.Sound(os.path.join(sounds_path, "wump.wav")),
            "surprise": pygame.mixer.Sound(os.path.join(sounds_path, "surprise.wav"))
        }

    def get_image(self, image_name):
        return self.images.get(image_name)

    def play_sound(self, voice_name):
        self.sounds[voice_name].play()