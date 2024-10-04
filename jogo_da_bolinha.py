import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definições de cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)

# Dimensões da tela
LARGURA = 800
ALTURA = 600

# Criar a tela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo da Bolinha")

# Propriedades da bolinha
raio_bolinha = 15

def reiniciar_bolinha():
    return [LARGURA // 2, ALTURA // 2], [random.choice([-10, 10]), random.choice([-10, 10])]

posicao_bolinha, velocidade_bolinha = reiniciar_bolinha()

# Propriedades das barras
largura_barra = 15
altura_barra = 100
posicao_barra_esquerda = [10, (ALTURA - altura_barra) // 2]
posicao_barra_direita = [LARGURA - 20, (ALTURA - altura_barra) // 2]

# Controle da barra
velocidade_barra = 5

# Pontuação
pontos_esquerda = 0
pontos_direita = 0

# Fonte para exibir a pontuação
fonte = pygame.font.Font(None, 74)

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Controle das barras
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and posicao_barra_esquerda[1] > 0:  # Barra esquerda para cima
        posicao_barra_esquerda[1] -= velocidade_barra
    if teclas[pygame.K_s] and posicao_barra_esquerda[1] < ALTURA - altura_barra:  # Barra esquerda para baixo
        posicao_barra_esquerda[1] += velocidade_barra
    if teclas[pygame.K_UP] and posicao_barra_direita[1] > 0:  # Barra direita para cima
        posicao_barra_direita[1] -= velocidade_barra
    if teclas[pygame.K_DOWN] and posicao_barra_direita[1] < ALTURA - altura_barra:  # Barra direita para baixo
        posicao_barra_direita[1] += velocidade_barra

    # Movimentação da bolinha
    posicao_bolinha[0] += velocidade_bolinha[0]
    posicao_bolinha[1] += velocidade_bolinha[1]

    # Colisão com as extremidades da tela
    if posicao_bolinha[1] <= raio_bolinha or posicao_bolinha[1] >= ALTURA - raio_bolinha:
        velocidade_bolinha[1] = -velocidade_bolinha[1]

    # Colisão com as barras
    if (posicao_bolinha[0] - raio_bolinha <= posicao_barra_esquerda[0] + largura_barra and
        posicao_barra_esquerda[1] < posicao_bolinha[1] < posicao_barra_esquerda[1] + altura_barra):
        velocidade_bolinha[0] = -velocidade_bolinha[0]
    elif (posicao_bolinha[0] + raio_bolinha >= posicao_barra_direita[0] and
          posicao_barra_direita[1] < posicao_bolinha[1] < posicao_barra_direita[1] + altura_barra):
        velocidade_bolinha[0] = -velocidade_bolinha[0]
    elif posicao_bolinha[0] < 0:  # Bolinha sai pela esquerda
        pontos_direita += 1
        posicao_bolinha, velocidade_bolinha = reiniciar_bolinha()
    elif posicao_bolinha[0] > LARGURA:  # Bolinha sai pela direita
        pontos_esquerda += 1
        posicao_bolinha, velocidade_bolinha = reiniciar_bolinha()

    # Desenhar tudo
    tela.fill(PRETO)
    pygame.draw.circle(tela, VERDE, (posicao_bolinha[0], posicao_bolinha[1]), raio_bolinha)
    pygame.draw.rect(tela, BRANCO, (posicao_barra_esquerda[0], posicao_barra_esquerda[1], largura_barra, altura_barra))
    pygame.draw.rect(tela, BRANCO, (posicao_barra_direita[0], posicao_barra_direita[1], largura_barra, altura_barra))

    # Exibir a pontuação
    texto = fonte.render(f"{pontos_esquerda} | {pontos_direita}", True, BRANCO)
    tela.blit(texto, (LARGURA // 2 - texto.get_width() // 2, 20))

    pygame.display.flip()
    pygame.time.delay(30)

# Finaliza o Pygame
pygame.quit()
