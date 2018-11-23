from hero import *
from botao import Botao
import pygame.mixer

pygame.init()
ImagemFundo = pygame.image.load('Imagens/Temple/temple.png')
ImagemTemplo = pygame.image.load('Imagens/Temple/Dentro.png')
ImagemGame1 = pygame.image.load('Imagens/Temple/Game1.png')
ImagemGame2 = pygame.image.load('Imagens/Temple/Game2.png')
ImagemGame3 = pygame.image.load('Imagens/Temple/Game3.png')
ImagemFim = pygame.image.load('Imagens/FIM.png')



pygame.mixer.music.load('Som/musica.mp3')
pygame.mixer.music.play(-1)
tela = pygame.display.set_mode((1024, 576))
tela.blit(ImagemFundo, (0,0))

pygame.display.set_caption("Path of Ordenation")
contador = 0

listaSprites = pygame.sprite.Group()
hero = Hero(40, 430)



bt1 = pygame.image.load('Imagens/Buttons/bt1.png').convert_alpha()
bt2 = pygame.image.load('Imagens/Buttons/bt2.png').convert_alpha()
bt3 = pygame.image.load('Imagens/Buttons/bt3.png').convert_alpha()
bt4 = pygame.image.load('Imagens/Buttons/bt4.png').convert_alpha()
bt5 = pygame.image.load('Imagens/Buttons/bt5.png').convert_alpha()
bt6 = pygame.image.load('Imagens/Buttons/bt6.png').convert_alpha()
bt7 = pygame.image.load('Imagens/Buttons/bt7.png').convert_alpha()
bt8 = pygame.image.load('Imagens/Buttons/bt8.png').convert_alpha()
bt9 = pygame.image.load('Imagens/Buttons/bt9.png').convert_alpha()

botao1 = Botao(106, 320, bt3, 3)
botao2 = Botao(412, 150, bt1, 1)
botao3 = Botao(718, 320, bt2, 2)

botao4 = Botao(106, 320, bt5, 2)
botao5 = Botao(412, 150, bt4, 3)
botao6 = Botao(718, 320, bt6, 1)

botao7 = Botao(106, 320, bt9, 3)
botao8 = Botao(412, 150, bt8, 1)
botao9 = Botao(718, 320, bt7, 2)

chave1 = []
chave2 = []
chave3 = []

sair = False

ganhou1 = False
ganhou2 = False
ganhou3 = False

while not sair:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True

        if event.type == pygame.KEYDOWN:
            tecla = pygame.key.get_pressed()

            if tecla[pygame.K_SPACE]:
                listaSprites.add(hero)
                morreu = False
                while not morreu:
                    for event in pygame.event.get():
                        time.sleep(0.1)
                        hero.mudarImagem()

                        if event.type == pygame.QUIT:
                            sair = True
                            morreu = True

                        if event.type == pygame.KEYDOWN:
                            tecla = pygame.key.get_pressed()

                            if tecla[pygame.K_LEFT]:
                                hero.andarEsq()

                            if tecla[pygame.K_RIGHT]:
                                hero.andarDir()

                        if hero.x1 >= 520:
                            listaSprites.remove(hero)
                            tela.blit(ImagemGame1, (0, 0))
                            contador = 0
                            listaSprites.add(botao1)
                            listaSprites.add(botao2)
                            listaSprites.add(botao3)
                            while not ganhou1:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        ganhou1 = True
                                        ganhou2 = True
                                        ganhou3 = True
                                        morreu = True
                                        sair = True

                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        mx, my = pygame.mouse.get_pos()
                                        if (mx >= 106 and mx <= 306 and my >= 320 and my <= 420):
                                            chave1.append(botao1.valor)
                                            contador += 1
                                            listaSprites.remove(botao1)
                                            botao1.clicar()

                                        if (mx >= 412 and mx <= 612 and my >= 150 and my <= 250):
                                            chave1.append(botao2.valor)
                                            contador += 1
                                            listaSprites.remove(botao2)
                                            botao2.clicar()

                                        if (mx >= 718 and mx <= 918 and my >= 320 and my <= 420):
                                            chave1.append(botao3.valor)
                                            listaSprites.remove(botao3)
                                            botao3.clicar()
                                            contador += 1

                                        if contador == 3:
                                            if chave1[0] == 1 and chave1[1] == 2 and chave1[2] == 3:
                                                print("ganhou")
                                                listaSprites.add(botao4)
                                                listaSprites.add(botao5)
                                                listaSprites.add(botao6)
                                                tela.blit(ImagemGame2, (0, 0))
                                                ganhou1 = True
                                            elif chave1[0] != 1 or chave1[1] != 2 or chave1[2] != 3:
                                                contador = 0
                                                chave1.clear()
                                                listaSprites.add(botao1)
                                                listaSprites.add(botao2)
                                                listaSprites.add(botao3)
                                                ganhou1 = False
                                tela.blit(ImagemGame1, (0, 0))
                                listaSprites.draw(tela)
                                pygame.display.update()
                            while not ganhou2:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        ganhou1 = True
                                        ganhou2 = True
                                        ganhou3 = True
                                        morreu = True
                                        sair = True

                                    if event.type == pygame.MOUSEBUTTONDOWN:

                                        mx, my = pygame.mouse.get_pos()
                                        if (mx >= 106 and mx <= 306 and my >= 320 and my <= 420):
                                            chave2.append(botao4.valor)
                                            contador += 1
                                            listaSprites.remove(botao4)
                                            botao4.clicar()

                                        if (mx >= 412 and mx <= 612 and my >= 150 and my <= 250):
                                            chave2.append(botao5.valor)
                                            contador += 1
                                            listaSprites.remove(botao5)
                                            botao5.clicar()

                                        if (mx >= 718 and mx <= 918 and my >= 320 and my <= 420):
                                            chave2.append(botao6.valor)
                                            listaSprites.remove(botao6)
                                            botao6.clicar()
                                            contador += 1

                                        if contador == 6:
                                            if chave2[0] == 1 and chave2[1] == 2 and chave2[2] == 3:
                                                print("ganhou2")
                                                listaSprites.add(botao7)
                                                listaSprites.add(botao8)
                                                listaSprites.add(botao9)
                                                tela.blit(ImagemGame3, (0,0))
                                                ganhou2 = True
                                            elif chave2[0] != 1 or chave2[1] != 2 or chave2[2] != 3:
                                                chave2.clear()
                                                contador = 3
                                                listaSprites.add(botao4)
                                                listaSprites.add(botao5)
                                                listaSprites.add(botao6)
                                                ganhou2 = False

                                tela.blit(ImagemGame2, (0, 0))
                                listaSprites.draw(tela)
                                pygame.display.update()

                            while not ganhou3:
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        ganhou1 = True
                                        ganhou2 = True
                                        ganhou3 = True
                                        morreu = True
                                        sair = True

                                    if event.type == pygame.MOUSEBUTTONDOWN:

                                        mx, my = pygame.mouse.get_pos()
                                        if (mx >= 106 and mx <= 306 and my >= 320 and my <= 420):
                                            chave3.append(botao7.valor)
                                            contador += 1
                                            listaSprites.remove(botao7)
                                            botao7.clicar()

                                        if (mx >= 412 and mx <= 612 and my >= 150 and my <= 250):
                                            chave3.append(botao8.valor)
                                            contador += 1
                                            listaSprites.remove(botao8)
                                            botao8.clicar()

                                        if (mx >= 718 and mx <= 918 and my >= 320 and my <= 420):
                                            chave3.append(botao9.valor)
                                            listaSprites.remove(botao9)
                                            botao9.clicar()
                                            contador += 1

                                        if contador == 9:
                                            if chave3[0] == 1 and chave3[1] == 2 and chave3[2] == 3:
                                                print("ganhou3")
                                                ganhou3 = True


                                            elif chave3[0] != 1 or chave3[1] != 2 or chave3[2] != 3:
                                                chave3.clear()
                                                contador = 6
                                                listaSprites.add(botao7)
                                                listaSprites.add(botao8)
                                                listaSprites.add(botao9)
                                                ganhou3 = False
                                tela.blit(ImagemGame3, (0, 0))
                                listaSprites.draw(tela)
                                pygame.display.update()

                            if ganhou3 == True:
                                while not sair:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            morreu = True
                                            sair = True
                                    tela.blit(ImagemFim, (0, 0))
                                    pygame.display.update()

                    tela.blit(ImagemTemplo, (0, 0))
                    listaSprites.draw(tela)
                    pygame.display.update()
                morreu = True
                sair = True

    tela.blit(ImagemFundo, (0, 0))
    pygame.display.update()

pygame.quit()