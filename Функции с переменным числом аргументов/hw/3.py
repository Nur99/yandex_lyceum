def find_farthest_orbit(list_of_orbits):
    planet_orbits = [orbit for orbit in list_of_orbits if orbit[0] != orbit[1]]
    max_area = max([3.14 * a * b for a, b in planet_orbits])
    max_orbits = [(a, b) for a, b in planet_orbits if 3.14 * a * b == max_area]
    return max_orbits[0]

