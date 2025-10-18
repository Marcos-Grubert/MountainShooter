import pygame

print('Jogo Iniciado')
pygame.init()
window = pygame.display.set_mode(size=(800, 600))
print('Jogo Encerrado')

print('Loop Iniciado')
while True:
    #Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Close window
            quit() #Stop Pygame