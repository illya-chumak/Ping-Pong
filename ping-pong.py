from pygame import *
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))

class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, width=65, height=65):
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed # швидкість переміщення спрайту
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x # координата x спрайту
        self.rect.y = player_y # координата y спрайту

    # метод для відображення спрайту у точці з координатами (x, y)
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 155:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 155:
            self.rect.y += self.speed
back = (200, 255, 255)  # колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
game = True
finish = False
clock = time.Clock()
FPS = 60
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tennis_ball.png', 200, 200, 4, 50, 50)
speedx=3
speedy=3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(back)

        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speedx
        ball.rect.y += speedy

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speedx *= -1
            speedy *= 1

        # якщо м'яч досягає меж екрана, змінюємо напрямок його руху
        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speedy *= -1

        # якщо м'яч відлетів далі ракетки, виводимо умову програшу для першого гравця
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        # якщо м'яч полетів далі ракетки, виводимо умову програшу другого гравця
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)