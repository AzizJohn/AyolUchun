import os
import secrets
import string
from os.path import exists

from PIL import Image, ImageDraw, ImageFont

from core.settings import BASE_DIR

WEBSITE = 'https://uic.group'
FONT = os.path.join(BASE_DIR, 'media', 'MTCORSVA.TTF')

CERTIFICATE = os.path.join(BASE_DIR, 'media', 'certificate.jpg')

CER_DIR = f'{BASE_DIR}/'


def generate_name():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(5))

    return password


def certificate_generate(user, course):
    print(user.first_name, user.last_name, course.title, course.text_for_certificate)
    text_y_position = 1300
    img = Image.open(CERTIFICATE, mode='r')
    image_width = img.width
    image_height = img.height
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT, size=150)
    text_width = draw.textlength(f"{user.first_name} {user.last_name}", font=font)
    draw.text(
        (1700, text_y_position - 300), course.title, font=ImageFont.truetype(FONT, size=120), fill="#000000"
    )
    draw.text(
        ((image_width + 1370 - text_width - (image_width - 3200)) / 2, text_y_position), user.first_name, font=font, fill="#0e89c4"
    )
    draw.text(
        (1550, text_y_position + 200), course.text_for_certificate, font=ImageFont.truetype(FONT, size=120),
        fill="#000000"
    )

    if exists(os.path.join(CER_DIR, 'media', 'certificate')) == False:
        os.makedirs(os.path.join(CER_DIR, 'media', 'certificate'))
    file_name = f"{user.first_name} {user.last_name}.jpg"
    save_img_path = os.path.join(CER_DIR, 'media', 'certificate', file_name)
    if exists(save_img_path):
        while True:
            file_name = f"{user.first_name} {user.last_name}{generate_name()}.jpg"
            save_img_path = os.path.join(CER_DIR, 'media', 'certificate', file_name)
            if exists(save_img_path):
                continue
            else:
                break
    img.save(save_img_path)

    return os.path.join('certificate', file_name)
