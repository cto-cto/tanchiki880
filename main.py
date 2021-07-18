import pygame
from objects import Player, TextureMove
from constants import WIDTH, HEIGHT, BLACK, FPS


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        pygame.display.set_caption('Platformer')
        # Создаем спрайт игрока
        self.player = Player(200, 200)
        self.texture = TextureMove(0,0, 'brickf')
        # создаем группу для всех спрайтов в игре
        self.all_sprite_list = pygame.sprite.Group()
        self.all_sprite_list.add(self.player)
        self.all_sprite_list.add(self.texture)
        self.clock = pygame.time.Clock()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprite_list.draw(self.screen)

    def run(self):
        done = False
        while not done:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    texture = self.texture.place()
                    self.all_sprite_list.add(texture)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.go_left()
                    elif event.key == pygame.K_q:
                        self.texture.change_img(input('Текстура: '))
                    elif event.key == pygame.K_RIGHT:
                        self.player.go_right()
                    elif event.key == pygame.K_UP:
                        self.player.go_up()
                    elif event.key == pygame.K_DOWN:
                        self.player.go_down()
                    elif event.key == pygame.K_SPACE:
                        bullet = self.player.shoot()
                        if bullet:
                            self.all_sprite_list.add(bullet)

                elif event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                        self.player.stop()

            self.draw()
            self.all_sprite_list.update()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()


game = Game()
game.run()
