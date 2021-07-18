import os
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.change_x = 0
        self.change_y = 0
        self._load_img('assets/tank_gold1.png')
        self.direction = 'U'
        self.image = self.image_u
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.cooldown = 0

    def _load_img(self, path):
        self.image_u = pygame.image.load(path)
        self.image_l = pygame.transform.rotate(self.image_u, 90)
        self.image_r = pygame.transform.rotate(self.image_u, -90)
        self.image_d = pygame.transform.flip(self.image_u, False, True)

        self.direct_dict = {
            'R':  self.image_r,
            'L': self.image_l,
            'D': self.image_d,
            'U': self.image_u,
        }

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.image = self.direct_dict[self.direction]
        if self.cooldown > 0:
            self.cooldown -= 1

    # Движение, управляемое игроком:
    def go_left(self):
        """ Вызывается, когда пользователь нажимает стрелку влево. """
        self.change_x -= 6
        self.direction = "L"

    def go_right(self):
        """ Вызывается, когда пользователь нажимает стрелку вправо. """
        self.change_x += 6
        self.direction = "R"

    def go_up(self):
        self.change_y -= 6
        self.direction = 'U'

    def go_down(self):
        self.change_y += 6
        self.direction = 'D'

    def stop(self):
        """Вызывается, когда пользователь отпускает клавиатуру. """
        self.change_x = 0
        self.change_y = 0

    def shoot(self):
        if self.cooldown == 0:
            self.cooldown = 30
            if self.direction == 'R':
                return Bullet(self.rect.x+65, self.rect.y+31, self.direction)
            if self.direction == 'L':
                return Bullet(self.rect.x-15, self.rect.y+26, self.direction)
            if self.direction == 'U':
                return Bullet(self.rect.x+33, self.rect.y-15, self.direction)
            if self.direction == 'D':
                return Bullet(self.rect.x+33, self.rect.y+65, self.direction)


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        super().__init__()
        self.change_x = 0
        self.change_y = 0

        if direction == 'R':
            self.change_x = 10
        if direction == 'L':
            self.change_x = -10
        if direction == 'U':
            self.change_y = -10
        if direction == 'D':
            self.change_y = 10

        self._load_img('assets/bullet.png')
        self.image = self.direct_dict[direction]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def _load_img(self, path):
        self.image_u = pygame.image.load(path)
        self.image_l = pygame.transform.rotate(self.image_u, 90)
        self.image_r = pygame.transform.rotate(self.image_u, -90)
        self.image_d = pygame.transform.flip(self.image_u, False, True)

        self.direct_dict = {
            'R':  self.image_r,
            'L': self.image_l,
            'D': self.image_d,
            'U': self.image_u,
        }

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y


class Texture(pygame.sprite.Sprite):
    def __init__(self, x, y, img_name):
        super().__init__()
        path = os.path.join('assets', 'texture', img_name+'.png')
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class TextureMove(Texture):
    def __init__(self, x, y, img_name):
        super().__init__(x, y, img_name)
        self.img_name = img_name

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.rect.x = x
        self.rect.y = y

    def change_img(self, img_name):
        self.img_name = img_name
        path = os.path.join('assets', 'texture', img_name+'.png')
        try:
            self.image = pygame.image.load(path)
        except FileNotFoundError:
            print('Нет такого файла, поробуй еще')


    def place(self):
        return Texture(self.rect.x, self.rect.y, self.img_name)