import os

import requests
import pygame

coordinates = input()
size = input()


def geocode(coordinates, size, type_map):
    map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + coordinates + "&z=" + size + "&l=" + type_map
    response = requests.get(map_request)
    return response.content


map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(geocode(coordinates, size))

try:
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()

    os.remove(map_file)
except Exception:
    print('неверный тип данных')
