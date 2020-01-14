def make_shades(alley, k):
    distance = len(alley)
    shades = [False] * distance
    for position in range(distance):
        height = alley[position]
        if height > 0:
            if k >= 0:
                start = position
                finish = min(position + k * height, distance - 1)
            else:
                start = max(position + k * height, 0)
                finish = position
            for shaded_place in range(start, finish + 1):
                shades[shaded_place] = True
    return shades


def calculate_sunny_length(shades):
    sum = 0
    for is_shaded in shades:
        if is_shaded:
            sum += 1
    return len(shades) - sum


def main():
    k = int(input())
    alley = [int(height) for height in input().split()]
    shades = make_shades(alley, k)
    if calculate_sunny_length(shades) >= 10:
        print("Обгорел")
    else:
        print("Тени достаточно")
