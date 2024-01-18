import pygame
# from time import sleep as czekaj

def is_prime_number(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    for i in range(2, round(number ** 0.5) + 1):
        if number / i == number // i:
            return False
    return True

def generate(n, step, x, y, steps):
    step_x, step_y = steps
    for s in range(step):
        if is_prime_number(n):
            pygame.draw.rect(ekran, color_yes, pygame.Rect(x, y, pixel_size, pixel_size))
            ekran.set_at((x, y), color_yes)
        n += 1
        x += step_x
        y += step_y
    pygame.display.flip()
    return (n, x, y)

def get_board_size(max_size):
    max_size -= 50
    while True:
        try:
            size = int(input(f'Board size (min 50 max {max_size}): '))
            if  50 <= size <= max_size: return size
        except:
            print('Enter a number only from the given range !!!')

def get_pixel_size(board_size):
    max_size = int(0.1 * board_size)
    while True:
        try:
            size = int(input(f'Pixel size (min 1 max {max_size}): '))
            if  1 <= size <= max_size: return size
        except:
            print('Enter a number only from the given range !!!')

pygame.init()
infoObject = pygame.display.Info()  # mus be before set_mode
max_size = max_hight = infoObject.current_h
max_width = infoObject.current_w
if max_size > max_width: max_size = max_width
scr_width = scr_hight = get_board_size(max_size)
ekran = pygame.display.set_mode((scr_width, scr_hight))
pixel_size = get_pixel_size(scr_width)  # or scr_hight
pygame.display.set_caption('*** Wykres liczb pierwszych ***')
ekran.fill((0,0,0))
color_yes = (255, 255, 255)
color_start = (255, 32, 32)
window_center = pygame.display.get_surface().get_rect().center
x_pos, y_pos = window_center
offset = pixel_size // 2
x_pos -= offset
y_pos -= offset
pygame.draw.rect(ekran, color_start, pygame.Rect(x_pos, y_pos, pixel_size, pixel_size))     # plot START pixel
#            x , y
step_xy = [( pixel_size,  0),
           ( 0         , pixel_size),
           (-pixel_size,  0),
           ( 0         , -pixel_size)]
number = 1
steps = 2
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    x_pos -= pixel_size
    y_pos -= pixel_size
    for i in range(4):
        if x_pos < 0:
            x_pos = 0
            steps -= 2
            break
        if y_pos < 0:
            y_pos = 0
            steps -= 2
            break
        number, x_pos, y_pos = generate(number, steps, x_pos, y_pos, step_xy[i])
    steps += 2

pygame.quit()
