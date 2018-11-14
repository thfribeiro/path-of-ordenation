import pygame
import time

class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()    #chama o construtor da superclasse
        self.parado = pygame.image.load('Imagens/Hero/Parado.png').convert_alpha()
        self.direita = pygame.image.load('Imagens/Hero/Direita.png').convert_alpha()
        self.esquerda = pygame.image.load('Imagens/Hero/Esquerda.png').convert_alpha()
        self.image = self.parado
        self.rect = self.image.get_rect()    # pega coordenadas
        self.rect.x = x
        self.rect.y = y
        self.x1 = x


    def andarDir(self):
        self.image = self.direita
        self.rect.x += 50
        self.x1 = self.rect.x

    def andarEsq(self):
        self.image = self.esquerda
        self.rect.x -= 10
        self.x1 = self.rect.x

    def mudarImagem(self):
        time.sleep(0.01)
        self.image = self.parado