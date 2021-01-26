from Samples.mapapi_PG import show_map


def show_moscow_stadiums():
    # Параметр позиционирования карты.
    moscow_location = "ll=37.622169,55.750493&spn=0.25,0.25"

    stadiums_location = {
        "Лужники": "37.554191,55.715551",
        "Спартак": "37.440262,55.818015",
        "Динамо": "37.559809,55.791540"
    }

    # Формируем параметр для рисования точек на карте.
    points = "~".join([pt for pt in stadiums_location.values()])
    points_param = f"pt={points}"

    show_map(moscow_location, "map", add_params=points_param)


def main():
    # Показать карту Москвы с точками на стадионах
    show_moscow_stadiums()


if __name__ == "__main__":
    main()
