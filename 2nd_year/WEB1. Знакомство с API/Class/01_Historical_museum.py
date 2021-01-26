from Samples.geocoder import geocode


def get_address_coords(address):
    # Ищем переданный адрес, ответ получаем в формате json.
    toponym = geocode(address)

    # Полный адрес топонима:
    toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    # Координаты центра топонима:
    toponym_coodrinates = toponym["Point"]["pos"]
    return toponym_coodrinates


def main():
    # Получение координат по адресу.
    for address in ["Москва, Красная площадь, 1"]:
        coords = get_address_coords(address)
        print(f"{address} имеет координаты: {coords}")
    print("")


if __name__ == "__main__":
    main()
