import pygame
import random
import sys

# Inicialização
pygame.init()

# Tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Desvie dos quadrados vermelhos!")

# Cores
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Fonte para o relógio
fonte = pygame.font.SysFont("Arial", 30)

# Jogador
jogador = pygame.Rect(LARGURA // 2, ALTURA // 2, 40, 40)
vel_jogador = 5

# Inimigos
inimigos = []
def adicionar_inimigo():
    x = random.randint(0, LARGURA - 40)
    y = random.randint(0, ALTURA - 40)
    dx = random.choice([-3, -2, -1, 1, 2, 3])
    dy = random.choice([-3, -2, -1, 1, 2, 3])
    inimigos.append({"rect": pygame.Rect(x, y, 40, 40), "vel": [dx, dy]})

# Começa com 5 inimigos
for _ in range(5):
    adicionar_inimigo()

# Relógio
clock = pygame.time.Clock()
tempo_inicio = pygame.time.get_ticks()
tempo_para_novo_inimigo = 5000  # 5 segundos
ultimo_spawn = tempo_inicio

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Tempo atual
    tempo_atual = pygame.time.get_ticks()
    segundos = (tempo_atual - tempo_inicio) // 1000

    # Adicionar novo inimigo a cada 5 segundos
    if tempo_atual - ultimo_spawn >= tempo_para_novo_inimigo:
        adicionar_inimigo()
        ultimo_spawn = tempo_atual

    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jogador.left > 0:
        jogador.x -= vel_jogador
    if teclas[pygame.K_RIGHT] and jogador.right < LARGURA:
        jogador.x += vel_jogador
    if teclas[pygame.K_UP] and jogador.top > 0:
        jogador.y -= vel_jogador
    if teclas[pygame.K_DOWN] and jogador.bottom < ALTURA:
        jogador.y += vel_jogador

    # Movimento dos inimigos
    for inimigo in inimigos:
        inimigo["rect"].x += inimigo["vel"][0]
        inimigo["rect"].y += inimigo["vel"][1]

        # Rebater nas bordas
        if inimigo["rect"].left <= 0 or inimigo["rect"].right >= LARGURA:
            inimigo["vel"][0] *= -1
        if inimigo["rect"].top <= 0 or inimigo["rect"].bottom >= ALTURA:
            inimigo["vel"][1] *= -1

        # Colisão
        if jogador.colliderect(inimigo["rect"]):
            print(f"Game Over! Você sobreviveu por {segundos} segundos.")
            pygame.quit()
            sys.exit()

    # Desenhar fundo e elementos
    TELA.fill(PRETO)
    pygame.draw.rect(TELA, AZUL, jogador)
    for inimigo in inimigos:
        pygame.draw.rect(TELA, VERMELHO, inimigo["rect"])

    # Mostrar tempo na tela
    texto_tempo = fonte.render(f"Tempo: {segundos}s", True, BRANCO)
    TELA.blit(texto_tempo, (10, 10))

    pygame.display.update()
    clock.tick(60)
