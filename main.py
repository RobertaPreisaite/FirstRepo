import os
import glob
from PIL import Image
import webbrowser

check = 1
while check > 0:
    path = input("\nEnter the directory of images: ")
    if os.path.isdir(path):
        check -= 1
    else:
        print("Folder does not exist. Try again.")


list_of_paths = []

for image in glob.glob(path + "*"):
    list_of_paths.append(image)

print("_____________________________\n")
print("IMAGES OVERVIEW\n")

number_of_images = len(list_of_paths)
print("Total number of images checked:",number_of_images,"\n")

full_image_names = []
for directory in list_of_paths:
    full_image_names.append(directory.split("\\")[-1])

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


list_of_sizes = []

for path in list_of_paths:
    my_image = Image.open(path)
    (width, height) = my_image.size
    list_of_sizes.append(str(width)+"x"+str(height))


dimension_dict = {}

for image in list_of_sizes:
    if image in dimension_dict:
        dimension_dict[image] += 1
    else:
        dimension_dict[image] = 1

print("Folder contains:")
for (dimensions, count) in dimension_dict.items():
    print("\t",count,"image(s) with dimensions of",dimensions)

format_dict = {"squares": 0, "horizontal": 0, "vertical": 0}
for dimensions in dimension_dict.keys():
    width = int(dimensions.split("x")[0])
    height = int(dimensions.split("x")[1])
    if width == height:
        format_dict["squares"] += 1
    elif width > height:
        format_dict["horizontal"] += 1
    else:
        format_dict["vertical"] += 1
print()

for (formats, count) in format_dict.items():
    print(count,"images are",formats)
print()


class Format:
    """Class named format stores image format types and where 
    image of specific type can be used in digital advertising."""
    def __init__(self, format_name, format_appliance):
        self.name = format_name
        self.appliance = format_appliance

square = Format("square", "Instagram posts")
horizontal = Format("horizontal", "banners in articles")
vertical = Format("vertical", "Facebook stories")
print("Squares can be used as " + square.appliance + ".")
print("Horizontal images can be used as " + horizontal.appliance + ".")
print("Vertical images can be used as " + vertical.appliance + ".")
print()

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
print('The smallest image is "' + str(full_image_names[index_of_smallest]) + '".')
print('The largest image is "' + str(full_image_names[index_of_largest]) + '".')

print("\n_____________________________\n")
print("ERRORS\n")

incorrect_names = 0

for i in range(number_of_images):
    width_by_name = int(dimensions_from_names[i].split("x")[0])
    width_by_size = int(list_of_sizes[i].split("x")[0])
    height_by_name = int(dimensions_from_names[i].split("x")[1])
    height_by_size = int(list_of_sizes[i].split("x")[1])

    if width_by_name != width_by_size:
        w_difference = abs(width_by_name - width_by_size)
        incorrect_names += 1
        if w_difference % 10 == 1:
            print('Image named "' + full_image_names[i] 
            + '" differs by ' + str(w_difference) + ' pixel of width.')
        else:
            print('Image named "' + full_image_names[i] 
            + '" differs by ' + str(w_difference) + ' pixels of width.')

    if height_by_name != height_by_size:
        h_difference = abs(height_by_name - height_by_size)
        incorrect_names += 1
        if h_difference % 10 == 1:
            print('Image named "' + full_image_names[i]
            + '" differs by ' + str(h_difference) + ' pixel of height.')
        else:
            print('Image named "' + full_image_names[i] 
            + '" differs by ' + str(h_difference) + ' pixels of height.')  


check = 1
VALIDFORMATS = "ad_formats.txt"
while check > 0:
    check_req = input('''\nDo you want to check if every image meets ad format requirements?
Type "yes" or "no": ''')
    if check_req.lower() == "no":
        invalid_images = 0
        break

    elif os.path.isfile(VALIDFORMATS):
        check -= 1
        ad_formats = open(VALIDFORMATS, "r")
        valid_formats = []
        invalid_images = 0

        for line in ad_formats:
            valid_formats.append(line.strip())
        ad_formats.close()

        for i in range(number_of_images):
            if image not in valid_formats:
                invalid_images += 1
                print('Image "' + full_image_names[i] + '" does not met ad requirements.')
    else:
        print("File is not found. Try again.")
print("Number of unusable images:", invalid_images)

print("\n_____________________________\n")  
print("SUMMARY\n")

if incorrect_names == 0:
    print("Every single image dimensions match dimensions specified in image name.")
else:
    print(incorrect_names, "out of", number_of_images, "images are named incorrectly!\n")

if invalid_images != 0:
    print("Some images do not met ad requirements.")
    print("Open requirements?")
    wish = ""
    while (wish != "yes") and (wish != "no"):
        wish = input('Type "yes" or "no": ').lower()
    if wish == "yes":
        webbrowser.open("https://support.google.com/google-ads/answer/1722096")