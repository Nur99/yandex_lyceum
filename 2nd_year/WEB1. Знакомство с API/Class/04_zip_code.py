from Samples.geocoder import geocode


def get_address_postal_code(address):
    # Ищем переданный адрес, ответ получаем в формате json.
    toponym = geocode(address)
    # Извлекаем почтовый индекс.
    postal_code = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
    return postal_code


def main():
    # Определяем почтовый индекс по адресу.
    address = ""
    postal_code = get_address_postal_code(address)
    print(f"{address} имеет индекс: {postal_code}")


if __name__ == "__main__":
    main()
