import pygame
import sys

# Configurações do jogo
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BALL_SPEED = [4, 4]
PADDLE_SPEED = 6

# Inicialização do pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Raquetes e bola
paddle_width, paddle_height = 10, 100
ball_size = 15

player1 = pygame.Rect(50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
player2 = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2, ball_size, ball_size)

ball_dx, ball_dy = BALL_SPEED
score1, score2 = 0, 0

def reset_ball():
    global ball_dx, ball_dy
    ball.x, ball.y = WIDTH // 2 - ball_size // 2, HEIGHT // 2 - ball_size // 2
    ball_dx *= -1

def update_scores():
    with open("pontuacoes.txt", "a") as file:
        file.write(f"Jogador 1: {score1} - Jogador 2: {score2}\n")

# Loop principal
going = True
while going:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            update_scores()
            going = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += PADDLE_SPEED

    # Movimento da bola
    ball.x += ball_dx
    ball.y += ball_dy

    # Colisão com as paredes
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Colisão com as raquetes
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_dx *= -1

    # Pontuação
    if ball.left <= 0:
        score2 += 1
        reset_ball()
    if ball.right >= WIDTH:
        score1 += 1
        reset_ball()

    # Desenhar objetos
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
