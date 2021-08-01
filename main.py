import json
from collections import defaultdict
import pygame
from objects import Player, TextureMove, Texture
from constants import WIDTH, HEIGHT, FPS


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.bg = pygame.image.load('bg.png')
        pygame.display.set_caption('Platformer')
        # Создаем спрайт игрока
        self.player = Player(200, 200)
        self.texture = TextureMove(0, 0, 'brickf')
        # создаем группу для всех спрайтов в игре
        self.sprite_list = pygame.sprite.Group()
        self.sprite_list.add(self.player)
        self.sprite_list.add(self.texture)
        self.clock = pygame.time.Clock()
        self.map = self.load_map()

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.sprite_list.draw(self.screen)

    def delete_texture(self, map):
        for t in self.sprite_list.sprites()[2:]:
            x, y = pygame.mouse.get_pos()
            w, h = t.rect.size
            if t.rect.x < x < t.rect.x + w and t.rect.y < y < t.rect.y + h:
                t.kill()
                for key in map:
                    for coord in map[key]:
                        if coord[0] == t.rect.x and coord[1] == t.rect.y:
                            map[key].pop(map[key].index(coord))

    def load_map(self):
        with open('map.json', 'r') as f:
            data = json.load(f)
        for key in data:
            for coords in data[key]:
                texture = Texture(*coords, key)
                self.sprite_list.add(texture)
        return data

    def run(self):
        done = False
        map = defaultdict(list, self.map)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    with open('map.json', 'w') as f:
                        json.dump(map, f)
                    done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        texture = self.texture.place()
                        self.sprite_list.add(texture)
                        map[self.texture.img_name].append(
                            (self.texture.rect.x, self.texture.rect.y))
                    if event.button == 3:
                        self.delete_texture(map)

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
                            self.sprite_list.add(bullet)

                elif event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                        self.player.stop()

            self.draw()
            self.sprite_list.update()
            pygame.display.flip()
            self.clock.tick(FPS)
        pygame.quit()


game = Game()
game.run()


# def add_texture(self, dict):
#     for k, v in dict.items():
#         self.img_name = k
#         for i in v:
#             self.sprite_list.add(Texture(i[0], i[1], k))
