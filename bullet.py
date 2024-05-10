import pygame


class Bullet:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("placeholder-sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .1

    def shoot(self,x_player, y_player):
        # take x and y of player and fire bullet from that point
        self.x = x_player
        self.y = y_player
        self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])