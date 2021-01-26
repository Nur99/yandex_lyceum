import sys

from Samples.distance import lonlat_distance
from Samples.geocoder import get_coordinates


def main():
    # Забираем две адресные точки из параметров запуска.
    address_1 = sys.argv[1]
    address_2 = sys.argv[2]

    # Получаем координаты двух введенных адресных точек
    address_1_point = get_coordinates(address_1)
    address_2_point = get_coordinates(address_2)
    print(lonlat_distance(address_1_point, address_2_point))


if __name__ == "__main__":
    main()
