import os.path
import time

from PIL import Image
import numpy as np

from Utilities.FileUtility import format_filename
from Utilities.ImageUtility import resize_image, write_ascii_to_file


def process_image():
    try:
        start = time.time()

        im = Image.open("ImageToProcess/maybelline.jpg")

        formatted_filename = format_filename(im.filename)

        print(f'File {im.filename} to be processed with initial size of {im.size}')

        if im.height > 350 or im.width > 350:
            im = resize_image(im)
        f = open('AsciiOutput/%s.txt' % formatted_filename, "w+")

        write_ascii_to_file(f, np.asarray(im))

        f.close()

        end = time.time()

        print(f'Time to process image of size {im.size}: {end-start} seconds')

    except FileNotFoundError:
        print('File not found')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_image()
