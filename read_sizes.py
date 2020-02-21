from PIL import Image

def read_sizes(list_of_paths):
    list_of_sizes = []
    for path in list_of_paths:
        my_image = Image.open(path)
        (width, height) = my_image.size
        list_of_sizes.append(str(width)+"x"+str(height))
    return list_of_sizes