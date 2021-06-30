import os.path
import time
from os import listdir
from os.path import isfile, join

from PIL import Image
import numpy as np

from Utilities.FileUtility import format_filename
from Utilities.ImageUtility import resize_image, write_ascii_to_file


def process_image():
    overall_start_time = time.time()
    folder_to_check = "ImageToProcess"
    images_to_process = [f for f in listdir(folder_to_check) if isfile(join(folder_to_check, f))]

    for image in images_to_process:
        image_start_time = time.time()
        im = Image.open("%s/%s" % (folder_to_check, image))
        formatted_filename = format_filename(im.filename)

        print(f'File {im.filename} to be processed with initial size of {im.size}')

        if im.height > 350 or im.width > 350:
            im = resize_image(im)
        f = open('AsciiOutput/%s.txt' % formatted_filename, "w+")

        write_ascii_to_file(f, np.asarray(im))

        f.close()
        image_end_time = time.time()
        print(f'Time to process image {formatted_filename} was {image_end_time - image_start_time} seconds')

    overall_end_time = time.time()

    print(f'Time to process {len(images_to_process)} image(s): {overall_end_time-overall_start_time} seconds')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_image()
