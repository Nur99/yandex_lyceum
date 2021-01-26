from Samples.geocoder import geocode


def get_address_component(town, component_index):
    # Ищем переданный адрес, ответ получаем в формате json.
    toponym = geocode(town)

    # Получаем компонентный адрес.
    components = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
    # Извлекаем из него запрошенный компонент (Страна, Округ, Область, Район, Город и т.д.) и его название.
    return components[component_index]["name"]


def main():
    # Определяем федеральный округ для города.
    for town in ["Хабаровск", "Уфа", "Нижний Новгород", "Калининград"]:
        province = get_address_component(town, 1)
        print(f"{town}: {province}")
    print("")


if __name__ == "__main__":
    main()
