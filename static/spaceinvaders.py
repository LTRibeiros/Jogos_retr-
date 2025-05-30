import pygame
import random
import sys

# === Inicialização ===
pygame.init()

# === Configurações ===
LARGURA, ALTURA = 640, 480
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Invaders Clone")

# === Cores ===
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
CINZA = (100, 100, 100)

# === Jogador ===
player_w, player_h = 50, 20
player_x = LARGURA // 2 - player_w // 2
player_y = ALTURA - player_h - 10
player_vel = 5

# === Balas ===
balas = []
bala_vel = 7
bala_w, bala_h = 4, 10

# === Inimigos ===
inimigos = []
inimigo_w, inimigo_h = 40, 20
inimigo_linhas = 3
inimigo_colunas = 7
inimigo_padding = 10
inimigo_vel_x = 1
inimigo_vel_y = 10
direcao = 1  # 1 direita, -1 esquerda

# === Balas dos inimigos ===
balas_inimigas = []
bala_inimiga_vel = 4

# === Barreiras ===
barreiras = []
barreira_w, barreira_h = 60, 30
barreira_y = ALTURA - 100
barreira_vidas = 10
for i in range(4):
    x = (i + 1) * LARGURA // 5 - barreira_w // 2
    barreiras.append({'rect': pygame.Rect(x, barreira_y, barreira_w, barreira_h), 'hp': barreira_vidas})

# === Criar inimigos ===
for linha in range(inimigo_linhas):
    for coluna in range(inimigo_colunas):
        x = coluna * (inimigo_w + inimigo_padding) + 50
        y = linha * (inimigo_h + inimigo_padding) + 50
        inimigos.append(pygame.Rect(x, y, inimigo_w, inimigo_h))

# === Clock ===
clock = pygame.time.Clock()

# === Fonte ===
fonte = pygame.font.SysFont('Arial', 24)

# === Funções ===
def desenhar_texto(texto, cor, x, y):
    img = fonte.render(texto, True, cor)
    TELA.blit(img, (x, y))

# === Loop Principal ===
rodando = True
while rodando:
    clock.tick(60)
    TELA.fill(PRETO)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bala = pygame.Rect(player_x + player_w // 2 - bala_w // 2, player_y, bala_w, bala_h)
                balas.append(bala)

    # === Movimentação do Jogador ===
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if teclas[pygame.K_RIGHT] and player_x < LARGURA - player_w:
        player_x += player_vel

    # === Movimentação das balas ===
    for bala in balas[:]:
        bala.y -= bala_vel
        if bala.y < 0:
            balas.remove(bala)

    for bala in balas_inimigas[:]:
        bala.y += bala_inimiga_vel
        if bala.y > ALTURA:
            balas_inimigas.remove(bala)

    # === Movimento dos inimigos ===
    move_descendo = False
    for inimigo in inimigos:
        inimigo.x += inimigo_vel_x * direcao
        if inimigo.right >= LARGURA or inimigo.left <= 0:
            move_descendo = True

    if move_descendo:
        direcao *= -1
        for inimigo in inimigos:
            inimigo.y += inimigo_vel_y

    # === Dificuldade dinâmica ===
    if len(inimigos) > 0:
        inimigo_vel_x = max(1, 3 - len(inimigos) // 5)

    # === Inimigos atirando ===
    if random.randint(0, 100) < 2 and len(inimigos) > 0:
        inimigo = random.choice(inimigos)
        bala = pygame.Rect(inimigo.x + inimigo_w // 2, inimigo.y + inimigo_h, bala_w, bala_h)
        balas_inimigas.append(bala)

    # === Colisão das balas do jogador ===
    for bala in balas[:]:
        for inimigo in inimigos[:]:
            if bala.colliderect(inimigo):
                balas.remove(bala)
                inimigos.remove(inimigo)
                break

    # === Colisão das balas inimigas ===
    for bala in balas_inimigas[:]:
        if pygame.Rect(player_x, player_y, player_w, player_h).colliderect(bala):
            # Game Over
            TELA.fill(PRETO)
            desenhar_texto("GAME OVER", VERMELHO, LARGURA // 2 - 80, ALTURA // 2)
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()
            sys.exit()

    # === Colisão com barreiras ===
    for barreira in barreiras:
        for bala in balas[:]:
            if barreira['rect'].colliderect(bala):
                balas.remove(bala)
                barreira['hp'] -= 1
        for bala in balas_inimigas[:]:
            if barreira['rect'].colliderect(bala):
                balas_inimigas.remove(bala)
                barreira['hp'] -= 1

    barreiras = [b for b in barreiras if b['hp'] > 0]

    # === Colisão inimigo com jogador ===
    for inimigo in inimigos:
        if inimigo.colliderect(pygame.Rect(player_x, player_y, player_w, player_h)):
            # Game Over
            TELA.fill(PRETO)
            desenhar_texto("GAME OVER", VERMELHO, LARGURA // 2 - 80, ALTURA // 2)
            pygame.display.update()
            pygame.time.delay(3000)
            pygame.quit()
            sys.exit()

    # === Vitória ===
    if len(inimigos) == 0:
        TELA.fill(PRETO)
        desenhar_texto("VOCÊ VENCEU!", VERDE, LARGURA // 2 - 100, ALTURA // 2)
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()

    # === Desenhar ===
    pygame.draw.rect(TELA, AZUL, (player_x, player_y, player_w, player_h))

    for bala in balas:
        pygame.draw.rect(TELA, VERDE, bala)

    for bala in balas_inimigas:
        pygame.draw.rect(TELA, VERMELHO, bala)

    for inimigo in inimigos:
        pygame.draw.rect(TELA, VERMELHO, inimigo)

    for barreira in barreiras:
        pygame.draw.rect(TELA, CINZA, barreira['rect'])
        desenhar_texto(str(barreira['hp']), BRANCO, barreira['rect'].x + 20, barreira['rect'].y + 5)

    desenhar_texto(f"Inimigos restantes: {len(inimigos)}", BRANCO, 10, 10)

    pygame.display.update()

pygame.quit()

