import pygame


class Bullet:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("placeholder-sprite.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .3

    def shoot(self,shoot_bullet):
        shoot_bullet = True
        return shoot_bullet

    def shoot_move(self):
        # take x and y of player and fire bullet from that point
        self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def find_player(self, x_player, y_player):
        self.x = x_player
        self.y = y_player
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])