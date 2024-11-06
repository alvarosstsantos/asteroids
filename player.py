import pygame
import circleshape
from constants import PLAYER_RADIUS


class Player(circleshape.CircleShape):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)

        self.__rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.__rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.__rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)