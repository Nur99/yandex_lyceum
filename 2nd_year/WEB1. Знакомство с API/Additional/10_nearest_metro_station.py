import sys

from Samples.geocoder import get_coordinates, get_nearest_object


def main():
    # Забираем адресную точку из параметров запуска.
    address = sys.argv[1]

    # Получаем координаты точки
    address_point = get_coordinates(address)

    # Получаем ближайшее метро.
    metro_name = get_nearest_object(address_point, "metro")

    if metro_name:
        print(f"Ближайшее к '{address}' - {metro_name}.")
    else:
        print(f"Рядом с '{address}' - метро нет.")


if __name__ == "__main__":
    main()
