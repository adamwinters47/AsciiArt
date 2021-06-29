from PIL import Image
import numpy as np


def process_image():
    try:
        im = Image.open("ImageInput/mario_test.jpg")
        print(f'File {im.filename} to be processed')
        print(f'Height: {im.height}px \nWidth: {im.width}px')

        pixel_matrix = np.asarray(im)
        # for row in pixel_matrix:
        #     for pixel in row:
        #         print(f'Pixel: {pixel}')
        #         for value in pixel:
        #             print(f'Value: {value}')

        # determine brightness of each pixel

        for row in pixel_matrix:
            for pixel in row:
                rgb_sum = 0
                for value in pixel:
                    rgb_sum += value
                brightness = rgb_sum / 3
                print(f'Brightness of pixel {pixel} is {brightness}')

        # tie brightness to an ascii character
        '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
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
