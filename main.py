import pygame
import random
import time
import sys
import colors
import config  # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events(screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
            elif event.key == pygame.K_SPACE:
                screen.fill(colors.WHITE)
                text_colors = [colors.BLUE, colors.RED, colors.GREEN, colors.BLACK, colors.PURPLE]
                text_options = ['Apollos', 'Eastman', 'Web & App', 'Hello!', 'Text']
                text_fonts = [
                    pygame.font.Font('FreeMono.ttf', random.randint(10, 75)),
                    pygame.font.Font('DejaVuSans.ttf', random.randint(10, 75))
                    ]
                     
                y = 100
                for text in text_options:
                    font = text_fonts[random.randint(0,1)]
                
                    if random.randint(0, 1) == 1:
                        font.set_bold(True)
                    else:
                        font.set_bold(False)

                    if random.randint(0, 1) == 1:
                        font.set_italic(True)
                    else:
                        font.set_italic(False)

                    text_surface = font.render(text, True, text_colors[random.randint(0,4)])
                    screen.blit(text_surface, (100, y))
                    y += 100
                
                pygame.display.flip()
    return True

def main():

    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock object
    screen.fill(colors.WHITE)
    pygame.display.flip()
    running = True
    while running:
        running = handle_events(screen)
          # Use color from config
        
        # Draw on the screen
        
        # Limit frame rate to certain number of frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
