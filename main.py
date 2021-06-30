import math

from PIL import Image
import numpy as np


def process_image():
    try:
        im = Image.open("ImageInput/starspittle-gmail-com.jpg")
        print(f'File {im.filename} to be processed')
        print(f'Height: {im.height}px \nWidth: {im.width}px')
        new_im = im.resize((math.floor(im.width/4), math.floor(im.height/4)))
        print(f'{new_im.size}')
        pixel_matrix = np.asarray(new_im)

        # determine brightness of each pixel
        ascii_text = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
        divisor = 255 / 65
        f = open('test.txt', "w+")
        for row in pixel_matrix:
            f.write('\n')
            for pixel in row:
                rgb_sum = 0
                for value in pixel:
                    rgb_sum += value
                brightness = rgb_sum / 3
                f.write("%s" % ascii_text[math.floor(brightness/divisor)-8]*3)
        f.close()
                # print(f'Brightness of pixel {pixel} is {brightness}')
        # tie brightness to an ascii character

        # put ascii character into grid

        # display image

        # save image to text file in output folder

        # place processed image into processed folder

        # remove image from input folder

    except FileNotFoundError:
        print('File not found')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    process_image()
