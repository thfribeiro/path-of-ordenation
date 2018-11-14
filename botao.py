import pygame

class Botao(pygame.sprite.Sprite):
    def __init__(self, x, y, fundobtn, valor):
        super().__init__()
        self.valor = valor
        self.imagem = fundobtn
        self.image = self.imagem
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def clicar(self):
            self.kill()
