from PIL import Image


def process_image():
    try:
        im = Image.open("ImageInput/mario_test.jpg")
        print(f'File {im.filename} to be processed')
        print(f'Height: {im.height}px \n Width: {im.width}px')
        dimensions = (im.height, im.width);
        print(f'{dimensions}')
        # first element of array should contain im.width num of elements, each element containing 3 values,
        # meaning the entire first element is the pixel values for every pixel in the first row ie: [(255, 255, 0),
        # (255, 255, 0)],   <- first row [(255, 255, 0), (255, 243, 0)]    <- second row & so on
        pixels = list(im.getdata())
        print(f'{pixels}')
        pixel_matrix = [[0 for x in range(im.width)] for y in range(im.height)]
        pixel_matrix[0][0] = 5
        print(f'{pixel_matrix[0][0]}')
        0 for i in range(im.height):
            0 for j in range(im.width):
                print(f'X: {x}\nY: {y}')
                pixel_matrix[x][y] = im.getpixel((x, y))
                print(f'{pixel_matrix[x][y]}')

        print(f'{pixel_matrix}')


        # determine brightness of each pixel

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
