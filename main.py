import time
from os import listdir
from os.path import isfile, join

from PIL import Image
import numpy as np

from Utilities.FileUtility import format_filename, file_cleanup
from Utilities.ImageUtility import resize_image, write_ascii_to_file


def process_image():
    overall_start_time = time.time()
    folder_to_check = "ImageToProcess"
    images_to_process = [f for f in listdir(folder_to_check) if isfile(join(folder_to_check, f))]

    for image in images_to_process:
        image_start_time = time.time()

        im = Image.open("%s/%s" % (folder_to_check, image))
        original_filename = im.filename
        print(f'File {original_filename} to be processed with initial size of {im.size}')

        formatted_filename = format_filename(original_filename)
        print(f'{im.format}')
        if im.format != "JPEG":
            print(f'Converting file {original_filename}')
            im = im.convert('RGB')

        max_image_size_in_pixels = 650
        if im.height > max_image_size_in_pixels or im.width > max_image_size_in_pixels:
            im = resize_image(im, max_image_size_in_pixels)
        f = open('AsciiOutput/%s.txt' % formatted_filename, "w+")

        write_ascii_to_file(f, np.asarray(im))

        f.close()
        file_cleanup(im, original_filename, formatted_filename)
        image_end_time = time.time()
        print(f'Time to process image {formatted_filename} was {image_end_time - image_start_time} seconds')

    overall_end_time = time.time()

    print(f'Time to process {len(images_to_process)} image(s): {overall_end_time-overall_start_time} seconds')


if __name__ == '__main__':
    process_image()
