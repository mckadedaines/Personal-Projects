import pygame

pygame.init()
pygame.font.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("First pixel game")
bg_color = (135, 206, 235)

font = pygame.font.Font(None, 36)

class Character(pygame.sprite.Sprite):
    IDLE = "idle"
    RUNNING = "running"
    ATTACKING = "attacking"
    JUMP = "jump"

    def __init__(self, sprite_sheet_path, sprite_width, sprite_height, columns):
        super().__init__()
        self.facing_right = True
        self.sprite_sheet = pygame.image.load("./pixel_art/adventurer-v1.5-Sheet.png").convert_alpha()
        self.frames = self.load_frames(sprite_width, sprite_height, columns)
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.bottom = 500 + 147 - self.image.get_height()
        self.v_speed = 0
        self.gravity = 1
        self.ground_y = 500 + 147 - self.image.get_height()
        self.jumping = False
        self.initiate_attack = False
        self.frame_delay = 5
        self.frame_counter = 0 
        self.animations = {
            self.IDLE: self.frames[0:4],
            self.RUNNING: self.frames[9:13],
            self.ATTACKING: self.frames[39:60],
            self.JUMP: self.frames[17:24]
        }
        self.state = self.IDLE

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        sprite = pygame.transform.scale(sprite, (width * 3, height * 3))
        return sprite

    def load_frames(self, sprite_width, sprite_height, columns):
        frames = []
        for y in range(0, self.sprite_sheet.get_height(), sprite_height):
            for x in range(0, columns * sprite_width, sprite_width):
                frames.append(self.get_sprite(x, y, sprite_width, sprite_height))
        return frames

    def update(self):
        self.frame_counter += 1
        current_animation = self.animations[self.state]
        if self.frame_counter >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(current_animation)
            self.image = current_animation[self.current_frame]
            if not self.facing_right:
                self.image = pygame.transform.flip(self.image, True, False)
            self.frame_counter = 0

    def move(self):
        key = pygame.key.get_pressed()
        speed = 10
        dx = 0
        dy = 0

        if key[pygame.K_a]:
            dx = -speed
            self.facing_right = False
            if not self.jumping:
                self.state = self.RUNNING
        if key[pygame.K_d]:
            dx = speed
            self.facing_right = True
            if not self.jumping:
                self.state = self.RUNNING
        if key[pygame.K_s]:
            dy = speed
            if not self.jumping:
                self.state = self.IDLE
        if key[pygame.K_SPACE] and (not self.jumping or self.rect.bottom == self.ground_y):
            self.v_speed = -15
            self.jumping = True
            self.state = self.JUMP

        if self.initiate_attack:
            self.state = self.ATTACKING
            self.reset_frame()
            self.initiate_attack = False

        if self.state == self.ATTACKING and self.current_frame == 0 and self.frame_counter == 0:
            if key[pygame.K_a] or key[pygame.K_d]:
                self.state = self.RUNNING
            else:
                self.state = self.IDLE

        if self.rect.left + dx < 0 or self.rect.right + dx > screen_width:
            dx = 0
        if self.rect.top + dy < 0 or self.rect.bottom + dy > self.ground_y:
            dy = 0

        self.rect.move_ip(dx, dy)
        self.v_speed += self.gravity
        self.rect.move_ip(0, self.v_speed)

    def reset_frame(self):
        self.current_frame = 0
        self.frame_counter = 0

    def screen_collision(self):
        key = pygame.key.get_pressed()
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
        elif self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom > self.ground_y:
            self.rect.bottom = self.ground_y
            self.v_speed = 0
            self.jumping = False
            if key[pygame.K_a] or key[pygame.K_d]:
                self.state = self.RUNNING
            else:
                self.state = self.IDLE

player = Character("./pixel_art/adventurer-v1.5-Sheet.png", 50, 37, columns=7)
dirt_block = pygame.image.load("./pixel_art/Main_Dirt_Block.png").convert_alpha()
clock = pygame.time.Clock()

def draw_platform(y_position, block_width_override=None):
    block_width = block_width_override or dirt_block.get_width()
    for x in range(-31, screen_width, block_width):
        screen.blit(dirt_block, (x, y_position))

run = True
while run:
    screen.fill(bg_color)
    player.update()
    screen.blit(player.image, player.rect.topleft)
    draw_platform(500, block_width_override=66)
    player.move()
    player.screen_collision() 

    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (0, 0, 0))
    screen.blit(fps_text, (screen_width - fps_text.get_width() - 10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.initiate_attack = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
