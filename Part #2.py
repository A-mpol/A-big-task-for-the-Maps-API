import os

import requests
import pygame

coordinates = input()
size = int(input())


def geocode(coordinates, size):
    map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + coordinates + "&z=" + str(size) + "&l=map"
    response = requests.get(map_request)
    return response.content


map_file = "map.png"

try:
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_PAGEUP]:
                    if size < 19:
                        size += 1
                if pygame.key.get_pressed()[pygame.K_PAGEDOWN]:
                    if size > 1:
                        size -= 1
        file = open(map_file, "wb")
        file.write(geocode(coordinates, size))
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()

    os.remove(map_file)
except Exception:
    print('неверный тип входных данных')