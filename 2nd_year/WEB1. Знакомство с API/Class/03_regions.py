from Samples.geocoder import geocode


def get_address_component(town, component_index):
    # Ищем переданный адрес, ответ получаем в формате json.
    toponym = geocode(town)

    # Получаем компонентный адрес.
    components = toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
    # Извлекаем из него запрошенный компонент (Страна, Округ, Область, Район, Город и т.д.) и его название.
    return components[component_index]["name"]


def main():
    # Определяем область/край/республику для города.
    for town in ["Барнаул", "Мелеуз", "Йошкар-Ола"]:
        area = get_address_component(town, 2)
        print(f"{town}: {area}")
    print("")


if __name__ == "__main__":
    main()
