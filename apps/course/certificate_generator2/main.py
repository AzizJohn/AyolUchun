from PIL import Image, ImageFont, ImageDraw

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
FONT_COLOR = "#FFFFFF"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size


def make_certificates(course, name):
    '''Function to save certificates as a .png file'''

    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)

    # Finding the width and height of the text. 
    name_width, name_height = draw.textsize(name.phone_number, font=FONT_FILE)

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name.phone_number, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./out/" + name.phone_number + ".png")
    print('Saving Certificate of:', name.phone_number)


# if __name__ == "__main__":
#
#     names = ["Azizjon Eshpulatov", 'Shaxzod Azamatov', 'Fazliddin Nabiyev']
#     for name in names:
#         make_certificates(name)
#
#     print(len(names), "certificates done.")
