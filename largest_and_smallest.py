def largest_and_smallest(number_of_images, list_of_sizes):
    areas = []

    for i in range(number_of_images):
        width = int(list_of_sizes[i].split("x")[0])
        height = int(list_of_sizes[i].split("x")[1])
        area = width * height
        areas.append(area)

    smallest_image = min(areas)
    largest_image = max(areas)
    index_of_smallest = areas.index(smallest_image)
    index_of_largest = areas.index(largest_image)

    return (index_of_smallest, index_of_largest)