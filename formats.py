def count_formats(list_of_sizes):
    dimension_dict = {}
    for image in list_of_sizes:
        if image in dimension_dict:
            dimension_dict[image] += 1
        else:
            dimension_dict[image] = 1
    return dimension_dict

def format_dict(dimension_dict):
    format_dict = {"squares": 0, "horizontal": 0, "vertical": 0}
    for dimensions, counts in dimension_dict.items():
        width = int(dimensions.split("x")[0])
        height = int(dimensions.split("x")[1])
        if width == height:
            format_dict["squares"] += (1 * counts)
        elif width > height:
            format_dict["horizontal"] += (1 * counts)
        else:
            format_dict["vertical"] += (1 * counts)
    return format_dict

class Format:
    """Class named format stores image format types and where 
    image of specific type can be used in digital advertising."""
    def __init__(self, format_name, format_appliance):
        self.name = format_name
        self.appliance = format_appliance

def format_appliance():
    square = Format("square", "Instagram posts")
    horizontal = Format("horizontal", "banners in articles")
    vertical = Format("vertical", "Facebook stories")

    whish = ""
    while whish != "yes" and whish != "no":
        whish = input("Do you want to see where these formats can be used? (yes/no): ").lower()
        if whish == "yes":
            print("Squares can be used as " + square.appliance + ".")
            print("Horizontal images can be used as " + horizontal.appliance + ".")
            print("Vertical images can be used as " + vertical.appliance + ".")