import pygame

class Jump_bar(pygame.sprite.Sprite):
    def __init__(self, amount):
        super().__init__()
        self.image=pygame.Surface((20, (100+(amount))*2))
        self.image.fill((100,200,0))
        self.rect=self.image.get_rect(topleft=(50,80))


    def jump_meter(self,amount):
        self.full=abs(amount)


class Jump_bar_bottom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((25, (210)))
        self.image.fill((0,0,0))
        self.rect=self.image.get_rect(topleft=(48,75))