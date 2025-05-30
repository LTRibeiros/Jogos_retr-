import pygame

pygame.init()

#--- coisas basicas -------------------------------------------------------------------------
tamanho_tela = (800,800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("braker")

tamanho_bola = 15
bola = pygame.Rect(392, 500, tamanho_bola, tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(350, 750, tamanho_jogador, 15)

qntd_blocos = 8
qntd_linhas = 5
qntd_total = qntd_blocos * qntd_linhas

largura = tamanho_tela[0] #q bosta de codigo
largurab = largura / qntd_blocos - 5 #dps mudar isso
nao = 2
def criar_blocos(qntd_blocos, qntd_linhas):
    altura = tamanho_tela[1]
    alturab = 15
    distancia_linhas = alturab + 10
    largura = tamanho_tela[0]
    largurab = largura / qntd_blocos - 5

    blocos = []
      
    for j in range(qntd_linhas):
        x = 2.5  
        for i in range(qntd_blocos):
            bloco = pygame.Rect(i * largurab + x , j * distancia_linhas, largurab, alturab)
            x = x + 5
            blocos.append(bloco)

    return blocos

cores = {
    "branca": (255, 255, 255),
    "preta": (0, 0, 0),
    "amarela": (255, 255, 0),
    "azul": (0, 0, 255),
    "verde": (0, 255, 0)
}

fim_jogo = False
vidas = 3
pnts = 0
velocidade = [2, -2]

#--- funcoes ---------------------------------------------------------------------------------
def movjogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            if (jogador.x + tamanho_jogador) < tamanho_tela[0]:
                jogador.x = jogador.x + nao
        if evento.key == pygame.K_LEFT:
            if jogador.x > 0:
                jogador.x = jogador.x - nao

    pass

def movbola(bola):
    movimento = velocidade
    bola.x = bola.x + movimento[0]
    bola.y = bola.y +  movimento[1]

    if bola.x <= 0:
        movimento[0] = -movimento[0]
    if bola.y <= 0:
        movimento[1] = -movimento[1]    
    if bola.x + tamanho_bola >= tamanho_tela[0]:
        movimento[0] = -movimento[0]
    if bola.y + tamanho_bola >= tamanho_tela[1]:
        movimento = None

    if jogador.collidepoint(bola.x, bola.y):
        movimento[1] = -movimento[1]
        if bola.x <= jogador.x:
            movimento[0] = -movimento[0]
        if bola.x >= jogador.x + tamanho_jogador:
            movimento[0] = -movimento[0]
    for bloco in blocos:
        if bloco.collidepoint(bola.x, bola.y):
            blocos.remove(bloco)
            movimento[1] = -movimento[1]
            if bola.x <= bloco.x:
                movimento[0] = -movimento[0]
            if bola.x >= bloco.x + largurab:
                movimento[0] = -movimento[0]

    return movimento

#--- "arte" ----------------------------------------------------------------------------------
def desenhar_inicio_jogo():
    tela.fill(cores["preta"])
    pygame.draw.rect(tela, cores["azul"], jogador)
    pygame.draw.rect(tela, cores["branca"], bola)

def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["verde"], bloco)

def desenhar_vidas(vidas):
    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f"vidas: {vidas}", 1, cores["amarela"])
    tela.blit(texto, (700, 780))

def pontuacao(pnts):
    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f"pontuação: {pnts * 100}", 1, cores["amarela"])
    tela.blit(texto, (0, 780))
    if pnts >= qntd_total:
        fonte = pygame.font.Font(None, 90)
        texto = fonte.render(f"ganhou", 1, cores["amarela"])
        tela.blit(texto, (350, 400))
    return pnts
    

blocos = criar_blocos(qntd_blocos, qntd_linhas)

#---- loop -----------------------------------------------------------------------------------

while not fim_jogo:
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)
    desenhar_vidas(vidas)
    pnts = pontuacao (qntd_total - len(blocos))
    if pnts >= qntd_total:
        vidas = 3
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True
    movjogador(evento)   
    if pnts >= 32 and nao == 2:
        nao = 4
        velocidade[0] = velocidade[0] * 2
        velocidade[1] = velocidade[0] * 2

    velocidade = movbola(bola)
    if velocidade == None:
        vidas = vidas - 1
        bola.x = 392
        bola.y = 500
        if nao == 2:
            velocidade = [2, -2]
        if nao == 4:
            velocidade = [4, -4]

    pygame.time.wait(1)
    pygame.display.flip()
    if vidas <= 0:
        fim_jogo = True

pygame.quit()