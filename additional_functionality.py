import os
import webbrowser

VALIDFORMATS = "ad_formats.txt"

def additional_functionality(number_of_images, full_image_names, list_of_sizes):
    check = 1
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
                if list_of_sizes[i] not in valid_formats:
                    invalid_images += 1
                    print('Image "' + full_image_names[i] + '" does not met ad requirements.')
        else:
            print("File is not found. Try again.")
    print()
    print("Number of unusable images:", invalid_images)
    return invalid_images

def open_requirements(invalid_images):
    if invalid_images != 0:
        print(invalid_images,"images do not met ad requirements.")
        print("Open requirements?")
        wish = ""
        while (wish != "yes") and (wish != "no"):
            wish = input('Type "yes" or "no": ').lower()
        if wish == "yes":
            webbrowser.open("https://support.google.com/google-ads/answer/1722096")
