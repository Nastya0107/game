import pygame
from add_to_game import Enemy_left, Enemy_bottom, Enemy_right, Enemy_top, Player, Bullet, Explosion, Bagroung

pygame.init()

width = 1366
height = 768
fps = 30
game_name = "Shooter"

BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"

snd_dir = "media/snd/"
img_dir = "media/img/"
icon = pygame.image.load(img_dir + 'icon.png')
pygame.display.set_icon(icon)
all_sprites = pygame.sprite.Group()
mobs_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()


pygame.mixer.music.load(snd_dir+"music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

bg = Bagroung()
all_sprites.add(bg)
enemy_bottom = Enemy_bottom()
enemy_left = Enemy_left()
enemy_right = Enemy_right()
enemy_top = Enemy_top()
player = Player()

player_sprite.add(player)
mobs_sprites.add([enemy_bottom, enemy_left, enemy_right, enemy_top])
all_sprites.add(player, enemy_bottom, enemy_left, enemy_right, enemy_top)

def draw_text(screen, text, size, x, y, color):
    font_name = pygame.font.match_font('arial')
    font = pygame.font.Font(font_name, size)
    text_image = font.render(text, True, color)
    text_rect = text_image.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_image, text_rect)

def new_mobs(count):
   for i in range(count):
       el = Enemy_left()
       er = Enemy_right()
       et = Enemy_top()
       eb = Enemy_bottom()
       all_sprites.add([el, er, et, eb])
       mobs_sprites.add([el, er, et, eb])

def draw_hp(screen, x, y, hp, hp_width, hp_height):       # Функция для рисования hp
    color = "#32CD32"                                     # Зеленый цвет
    white = "#FFFFFF"                                     # Белый цвет
    rect = pygame.Rect(x, y, hp_width, hp_height)         # Создаем рамку
    fill = (hp / 100) * hp_width                          # Считаем ширину полосы для hp
    fill_rect = pygame.Rect(x, y, fill, hp_height)        # Cоздаем полосу для hp

    pygame.draw.rect(screen, color, fill_rect)            # Рисуем полосу для hp
    pygame.draw.rect(screen, white, rect, 1)              # Рисуем рамку

def get_hit_sprite(hits_dict):
   for hit in hits_dict.values():
       return hit[0]

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)

timer = pygame.time.Clock()

def menu():
    screen.blit(bg.image, bg.rect)
    draw_text(screen, game_name, 128, width / 2, height / 4, WHITE)
    draw_text(screen, "Стрелки для движения, пробел - выстрел", 44,
              width / 2, height / 2, WHITE)
    draw_text(screen, "Нажмите любую кнопку для начала игры", 36, width / 2, height * 3 / 4, WHITE)
    pygame.display.flip()
    run = True
    while run:
        timer.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                run = False
attack = 1
killed = 0
game_over = True
run = True
level = 1
while run:
    if game_over:
        level = 1
        player.__init__()
        game_over = False
        menu()
    timer.tick(fps)
    all_sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player)
                all_sprites.add(bullet)
                bullets.add(bullet)
                player.snd_shoot.play()
    scratch = pygame.sprite.groupcollide(mobs_sprites, player_sprite, False, False)
    if scratch:
        sprite = get_hit_sprite(scratch)
        sprite.snd_scratch.play()
        player.hp -= attack
        if player.hp <= 0:
            game_over = True

    shots = pygame.sprite.groupcollide(bullets, mobs_sprites, True, False)
    if shots:
        sprite = get_hit_sprite(shots)
        sprite.hp -= 30
        if sprite.hp <= 0:
            sprite.snd_expl.play()
            expl = Explosion(sprite.rect.center)
            all_sprites.add(expl)
            sprite.kill()
            killed += 1
    if len(mobs_sprites) == 1:
        level += 1
        new_mobs(level)
        if level == 2:
            attack += 5
        elif level == 3:
            player.hp = 80
        elif level == 4:
            attack += 6
            player.hp = 50
    all_sprites.draw(screen)
    draw_hp(screen, 50, 50, player.hp, 200, 20)
    draw_text(screen, "Current Level: " + str(level), 50, 1189, 50, WHITE)
    draw_text(screen, "You killed " + str(killed) + " mobs", 50, 1120, 100, WHITE)
    pygame.display.update()
pygame.quit()