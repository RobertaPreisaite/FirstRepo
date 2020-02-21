import os
import glob
from PIL import Image
import webbrowser

import print_dashes_fun as PD
import read_names as RN
import read_sizes as RS
import formats
import largest_and_smallest as LS
import additional_functionality as AF

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

PD.print_dashes()
print("IMAGES OVERVIEW\n")

number_of_images = len(list_of_paths)
print("Total number of images checked:",number_of_images,"\n")


full_image_names = RN.full_names(list_of_paths)
dimensions_from_names = RN.dimensions_from_names(full_image_names)
list_of_sizes = RS.read_sizes(list_of_paths)

dimension_dict = formats.count_formats(list_of_sizes)

print("Folder contains:")
for (dimensions, count) in dimension_dict.items():
    print("\t",count,"image(s) with dimensions of",dimensions)
print()

format_dict = formats.format_dict(dimension_dict)

for (format, count) in format_dict.items():
    print(count,"images are",format)
print()

formats.format_appliance()
print()

(index_of_smallest, index_of_largest) = LS.largest_and_smallest(number_of_images, list_of_sizes)

print('The smallest image is "' + str(full_image_names[index_of_smallest]) + '".')
print('The largest image is "' + str(full_image_names[index_of_largest]) + '".')

PD.print_dashes()
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

invalid_images = AF.additional_functionality(number_of_images, full_image_names, image)

PD.print_dashes()
print("SUMMARY\n")

if incorrect_names == 0:
    print("Every single image dimensions match dimensions specified in image name.")
else:
    print(incorrect_names, "out of", number_of_images, "images are named incorrectly!\n")

AF.open_requirements(invalid_images)