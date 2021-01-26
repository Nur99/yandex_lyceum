import sys

from Samples.geocoder import geocode


def main():
    cities = sys.argv[1:]

    south_most_lattitude = 100.0  # Значение больше допустимого максимального (90 грд. С.Ш.) любой город точно южнее.
    south_most_city = ""

    for city in cities:
        # Находим город
        toponym = geocode(city)
        # Координаты центра топонима:
        toponym_coodrinates = toponym["Point"]["pos"]
        # Широта, преобразованная в плавающее число:
        toponym_lattitude = float(toponym_coodrinates.split(" ")[1])
        # Запоминаем самый южный город (с самой маленькой широтой) и его широту:
        if toponym_lattitude < south_most_lattitude:
            south_most_lattitude = toponym_lattitude
            south_most_city = city

    if south_most_city:
        print(south_most_city)


if __name__ == "__main__":
    main()
