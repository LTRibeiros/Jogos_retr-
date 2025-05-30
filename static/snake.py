import pygame
import random
import sys

# Inicialização do pygame
pygame.init()

# Configurações da tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game')

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
BRANCO = (255, 255, 255)

# Configurações do jogo
tamanho_bloco = 20
velocidade = 10

# Fonte
fonte = pygame.font.SysFont('arial', 30)


def mensagem(texto, cor, pos):
    texto_formatado = fonte.render(texto, True, cor)
    tela.blit(texto_formatado, pos)


def jogo():
    # Posição inicial da cobrinha
    x = largura // 2
    y = altura // 2
    dx = 0
    dy = 0

    # Lista para guardar o corpo da cobrinha
    corpo = []
    tamanho = 1

    # Gerar comida
    comida_x = round(random.randrange(0, largura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
    comida_y = round(random.randrange(0, altura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Movimento
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -tamanho_bloco
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = tamanho_bloco
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -tamanho_bloco
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = tamanho_bloco

        # Atualizar posição
        x += dx
        y += dy

        # Verificar colisão com bordas
        if x < 0 or x >= largura or y < 0 or y >= altura:
            break

        # Atualizar corpo
        cabeca = [x, y]
        corpo.append(cabeca)

        if len(corpo) > tamanho:
            del corpo[0]

        # Verificar colisão com o próprio corpo
        for segmento in corpo[:-1]:
            if segmento == cabeca:
                break

        # Verificar se comeu a comida
        if x == comida_x and y == comida_y:
            tamanho += 1
            comida_x = round(random.randrange(0, largura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco
            comida_y = round(random.randrange(0, altura - tamanho_bloco) / tamanho_bloco) * tamanho_bloco

        # Desenhar
        tela.fill(PRETO)
        for segmento in corpo:
            pygame.draw.rect(tela, VERDE, (segmento[0], segmento[1], tamanho_bloco, tamanho_bloco))

        pygame.draw.rect(tela, VERMELHO, (comida_x, comida_y, tamanho_bloco, tamanho_bloco))

        # Pontuação
        mensagem(f'Pontuação: {tamanho - 1}', BRANCO, (10, 10))

        pygame.display.update()
        clock.tick(velocidade)

    # Fim de jogo
    tela.fill(PRETO)
    mensagem('Game Over', VERMELHO, (largura // 2 - 80, altura // 2 - 20))
    mensagem(f'Pontuação: {tamanho - 1}', BRANCO, (largura // 2 - 80, altura // 2 + 20))
    pygame.display.update()
    pygame.time.delay(3000)


# Rodar o jogo
jogo()

