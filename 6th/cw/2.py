def simple_map(transformation, objects):
    result = []
    for object in objects:
        result.append(transformation(object))
    return result


# Можно поступить и совсем просто:
def simple_map(transformation, objects):
    return [transformation(obj) for obj in objects]

