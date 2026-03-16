from player import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    
    def update(self, dt):
        self.position+=self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event('asteroid_split')
            angle = random.uniform(20, 50)
            split_a = self.velocity.rotate(angle)
            split_b = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity= 1.2*split_a
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b.velocity=1.2*split_b
        