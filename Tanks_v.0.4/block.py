from pygame import *


class Block(sprite.Sprite):

    def __init__(self, topleft, filename, destructibility):
        sprite.Sprite.__init__(self)

        self.filename = filename

        self.image = image.load(self.filename)

        self.rect = self.image.get_rect()

        self.rect.topleft = topleft

        self.destructibility = destructibility
