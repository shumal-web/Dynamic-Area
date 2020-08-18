
import pygame


def main():
    white = (255, 255, 255)
    black = (0, 0, 0)
    pygame.init()
    font = pygame.font.Font(pygame.font.get_default_font(), 16)
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('Project phase 1')
    pygame.mouse.set_visible(0)
    thickness = 1
    height = ''

    def draw():
        area_of_square = int(height) * int(height)
        area_of_circle = int((3.14 * int(height) * int(height)) / 4)
        text_surface3 = font.render(f'Input Dimension : {height}', True, pygame.Color('orange'))
        text_surface = font.render(f'Area od square : {area_of_square}', True, pygame.Color('orange'))
        text_surface2 = font.render(f'Area of circle : {area_of_circle}', True, pygame.Color('orange'))

        screen.blit(text_surface, dest=(200, 600))
        screen.blit(text_surface2, dest=(600, 600))
        screen.blit(text_surface3, dest=(0, 600))
        pygame.draw.rect(screen, white, (100, 150, int(height), int(height)))
        pygame.draw.circle(screen, white, (700, 250), int(int(height) / 2))


    while True:
        screen.fill(black)
        text_surface4 = font.render('Area of square and circle ', True, pygame.Color('orange'))
        screen.blit(text_surface4, dest=(400, 0))
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            # stops the application
            break

        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            # gets the key name
            key_name = pygame.key.name(event.key)
            key_name = key_name.upper()

            # if any key is pressed
            if event.type == pygame.KEYDOWN:

                if key_name == 'BACKSPACE':
                    height = height[:-1]
                    text_surface4 = font.render('Please enter some value', True, pygame.Color('orange'))
                    if height == '':
                        screen.blit(text_surface4, dest=(0, 500))
                    else:
                        draw()

                    pygame.display.update()
                elif (key_name == '0' or key_name == '1' or key_name == '2' or key_name == '3' or key_name == '4'or key_name == '5' or key_name == '6' or key_name == '7' or key_name == '8' or key_name == '9' ):
                    height = height + key_name
                    text_surface4 = font.render('Please enter some value', True, pygame.Color('orange'))
                    if height == '':
                        screen.blit(text_surface4, dest=(0, 500))
                    else:
                        draw()

                    pygame.display.update()
                else:
                    pass

            elif event.type == pygame.KEYUP:
                pass
    pygame.quit()


if __name__ == '__main__':
    main()
