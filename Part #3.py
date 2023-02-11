import os

import requests
import pygame

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'

coordinates = input()
coordinates = [float(h) for h in coordinates.split(',')]
size = int(input())


def geocode(coordinates, size, type_map):
    coordinates = ','.join(str(h) for h in coordinates)
    map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + coordinates + "&z=" + str(size) + "&l=" + type_map
    response = requests.get(map_request)
    return response.content


def object_search(name_object):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}" \
                       f"&geocode={name_object}&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        return json_response


def object_coordinates(name_object):
    toponym = object_search(name_object)["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    return toponym["Point"]["pos"]


def moving(size):
    if 10 < size < 13:
        return size / (((size % 10) + size % 10) * 100)
    elif 13 < size < 18:
        return 0.005
    else:
        return 0.5


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
                if pygame.key.get_pressed()[pygame.K_RIGHT]:
                    if coordinates[0] < 179:
                        coordinates[0] += moving(size)
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                    if coordinates[0] > -179:
                        coordinates[0] -= moving(size)
                if pygame.key.get_pressed()[pygame.K_UP]:
                    if coordinates[1] < 89:
                        coordinates[1] += moving(size)
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                    if coordinates[1] > -89:
                        coordinates[1] -= moving(size)
        file = open(map_file, "wb")
        file.write(geocode(coordinates, size))
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()

    os.remove(map_file)
except Exception:
    print('неверный тип входных данных')
