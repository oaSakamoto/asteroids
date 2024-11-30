import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        old_radius = self.radius
        self.kill()

        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        radius = old_radius - ASTEROID_MIN_RADIUS
        
        asteroid_one = Asteroid(self.position.x, self.position.y, radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, radius)

        velocity_one = self.velocity.rotate(random_angle) * 1.2
        velocity_two = self.velocity.rotate(-random_angle) * 1.2

        asteroid_one.velocity = velocity_one
        asteroid_two.velocity = velocity_two
