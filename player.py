import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.change_x = 0
        self.change_y = 0
        self._load_tamk_img('assets/tank_gold1.png')
        self.direction = 'U'
        self.image = self.image_u
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def _load_tamk_img(self, path):
        self.image_u = pygame.image.load(path)
        self.image_l = pygame.transform.rotate(self.image_u, 90)
        self.image_r = pygame.transform.rotate(self.image_u, -90)
        self.image_d = pygame.transform.flip(self.image_u, False, True)
        self.direct_dict = {
            'R': self.image_r,
            'L': self.image_l,
            'D': self.image_d,
            'U': self.image_u,
        }

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.image = self.direct_dict[self.direction]

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
