from django.conf import settings
from imagekit import ImageSpec, register
from PIL import Image, ImageDraw, ImageFont

import os
import logging
logger = logging.getLogger(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))
#logger.error(dir_path)

#_default_font = ImageFont.truetype('../media/fonts/DejaVuSans-Bold.ttf', 42, encoding="unic")
_default_font = ImageFont.load_default()


def add_text_overlay(image, text, font=_default_font):
    rgba_image = image.convert('RGBA')
    text_overlay = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))

    image_draw = ImageDraw.Draw(text_overlay)
    text_size_x, text_size_y = image_draw.textsize(text, font=font)
    text_xy = ((rgba_image.size[0] / 2) - (text_size_x / 2), (rgba_image.size[1] / 2) - (text_size_y / 2))

    image_draw.text(text_xy, text, font=font, fill=(255, 255, 255, 128))
    image_with_text_overlay = Image.alpha_composite(rgba_image, text_overlay)

    return image_with_text_overlay


class TextOverlayProcessor(object):
    def __init__(self, text=None):
        """
        :param text: The overlay text, string.

        """
        self.text = text

    def process(self, img):
        return add_text_overlay(image=img, text=self.text)
