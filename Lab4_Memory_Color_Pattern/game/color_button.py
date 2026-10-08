import pygame
 
 
class ColorButton:
    """One pad of the 2x2 grid: dim when idle, bright when lit, owns its pitch."""
 
    def __init__(self, rect, base_color, lit_color, freq):
        self.rect = pygame.Rect(rect)
        self.base_color = base_color
        self.lit_color = lit_color
        self.freq = freq          # Task 3: each pad has its own pitch (Hz)
        self.lit = False
 
    def contains(self, pos):
        return self.rect.collidepoint(pos)
 
    def draw(self, screen):
        color = self.lit_color if self.lit else self.base_color
        pygame.draw.rect(screen, color, self.rect, border_radius=18)
        if self.lit:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 4, border_radius=18)
 