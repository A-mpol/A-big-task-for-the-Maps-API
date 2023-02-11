import requests

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


def geocode(coordinates, size, type_map):
    coordinates = ','.join(str(h) for h in coordinates)
    map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + coordinates + \
                  "&z=" + str(size) + \
                  "&l=" + type_map + \
                  "&pt=" + coordinates
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
