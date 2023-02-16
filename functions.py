import requests

API_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


def geocode(coordinates, size, type_map, pt=False):
    coordinates = ','.join(str(h) for h in coordinates)
    map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + coordinates + \
                  "&z=" + str(size) + \
                  "&l=" + type_map
    if pt:
        map_request += "&pt=" + coordinates
    response = requests.get(map_request)
    return response.content


def object_search(name_object):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}" \
                       f"&geocode={name_object}&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        return json_response


def get_toponym(name_object):
    data = object_search(name_object)
    return data["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]


def object_coordinates(name_object):
    toponym = get_toponym(name_object)
    return [float(cord) for cord in toponym["Point"]["pos"].split(' ')]


def full_address_object(name_object):
    toponym = get_toponym(name_object)
    return toponym['metaDataProperty']['GeocoderMetaData']['text']


def object_postal_code(name_object):
    toponym_country = get_toponym(name_object)["metaDataProperty"]["GeocoderMetaData"]["AddressDetails"]["Country"]
    return toponym_country["AdministrativeArea"]["Locality"]["Thoroughfare"]["Premise"]["PostalCode"]["PostalCodeNumber"]


def moving(size):
    if 10 < size < 13:
        return size / (((size % 10) + size % 10) * 100)
    elif 13 < size < 18:
        return 0.005
    else:
        return 0.5
