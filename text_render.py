from PIL import Image, ImageDraw, ImageFont
import numpy as np
from urllib.request import urlopen
import io
import os
import zipfile

font_files = {
    '5x5_pixel' : '/'.join([__file__.replace(os.sep, '/').rsplit('/', 1)[0], '5x5_pixel.ttf'])
}
font_urls = {
    '5x5_pixel' : ('https://dl.dafont.com/dl/?f=5x5_pixel', True, '5x5_pixel.ttf')
}


def render_text_columns(txt, font='5x5_pixel'):

    download_font_if_needed(font)

    # no idea why size has to be 7 here...
    pil_font = ImageFont.truetype(font_files[font], size=7)
    text_width, text_height = pil_font.getsize('A')

    res = []
    for c in txt:
        canvas = Image.new('1', [text_width, text_height], 0)
        draw = ImageDraw.Draw(canvas)
        draw.text((0, 0), c, font=pil_font, fill=1)
        a = np.asarray(canvas)
        res.extend(char_array_to_cols(a.transpose()))

    return res


def char_array_to_cols(arr):
    poweroftwos = np.array([2**i for i in range(arr.shape[1])])
    return np.sum(arr*poweroftwos, axis=1)


def download_font_if_needed(name):

    if name not in font_files:
        return None

    if not os.path.exists(font_files[name]):

        url, zipped, zip_path = font_urls[name]
        print('Downloading font {} from {}'.format(name, url))
        response = urlopen(url)
        data = io.BytesIO(response.read())

        if zipped:
            zipfile_ob = zipfile.ZipFile(data)
            data = zipfile_ob.open(zip_path)

        with open(font_files[name], 'wb') as fd:
            fd.write(data.read())


def main():
    print(font_files)
    print(font_urls)
    download_font_if_needed('5x5_pixel')

    print(char_array_to_cols(np.array([[True, False, False], [True, True, False], [False, False, True]])))
    print(render_text_columns('a'))


if __name__ == '__main__':
    main()

