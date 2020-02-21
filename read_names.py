def full_names(list_of_paths):
    full_image_names = []
    for directory in list_of_paths:
        full_image_names.append(directory.split("\\")[-1])
    return full_image_names

def dimensions_from_names(full_image_names):
    dimensions_from_names = []
    for name in full_image_names:
        x_index = name.find("x")
        while name[x_index + 1].isdigit() == False:
            x_index = name.find("x", x_index + 1)
        start_index = x_index - 1
        end_index = x_index + 1
        while name[start_index - 1].isdigit():
            start_index -= 1
        while name[end_index + 1].isdigit():
            end_index += 1
        dimensions_from_names.append(name[start_index : end_index + 1])
    return(dimensions_from_names)