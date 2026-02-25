import win32gui
import win32con
import win32api
import sys
import pygame
from random import randint
from convertPygamepic import convert

pygame.init()

# Load frames for animation

screen = pygame.display.set_mode((0, 0), pygame.NOFRAME)
folder = ""

frames = convert(folder)

frame_index = 0
frame_timer = 0

w, h = frames[0].get_width(), frames[0].get_height()

# Create a borderless window with the pet’s size
screen = pygame.display.set_mode((w, h), pygame.NOFRAME)
pygame.display.set_caption("Pet")

# Make the window transparent using a colorkey
hwnd = pygame.display.get_wm_info()["window"]
colorkey = (0, 255, 255)

win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) |
                       win32con.WS_EX_LAYERED |
                       win32con.WS_EX_TOPMOST)

win32gui.SetLayeredWindowAttributes(hwnd,
                                   win32api.RGB(*colorkey),
                                   0,
                                   win32con.LWA_COLORKEY)

clock = pygame.time.Clock()

dragging = False
mouse_offset = (0, 0)

def move_window(x, y):
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, w, h,
                          win32con.SWP_NOACTIVATE)


running = True
Doing_thing = False
x = 0
x, y = 0, 0  # Current Position max (-9001550),(-1500,1000)
xd ,yd = 500,500
move_window(x, y)
while running:
    print(x,y)
    if Doing_thing == False:
        x = randint(0,10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Start dragging
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            dragging = True
            mx, my = win32gui.GetCursorPos()
            mouse_offset = (mx - x, my - y)

        # Stop dragging
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False

    if x == 0:
        Doing_thing = True

    # Drag movement
    if dragging:
        x = 11
        mx, my = win32gui.GetCursorPos()
        x = mx - mouse_offset[0]
        y = my - mouse_offset[1]
        move_window(x, y)

    # Animation
    frame_timer += 1
    if frame_timer >= 8:
        frame_index = (frame_index + 1) % len(frames)
        frame_timer = 0

    # Draw using transparency colorkey
    screen.fill(colorkey)
    screen.blit(frames[frame_index], (0, 0))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()