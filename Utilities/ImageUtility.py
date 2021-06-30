import math


def resize_image(image):
    original_size = image.size
    while image.height > 350 or image.width > 350:
        image = image.reduce(2)
    print(f'Image reduced from {original_size} to {image.size}')
    return image

# ascii_text variable is a series of 65 characters that are on an ascending scale of brightness. The brightness of
# each pixel is determined with a weighted scale of RGB values. We then divide that brightness value by 3.95 to
# translate any number between 0 and 255 to a 64 character scale. We then grab the ascii character at that index and
# write it to the text file.
def write_ascii_to_file(file, image_pixel_matrix):
    ascii_text = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
    for row in image_pixel_matrix:
        file.write('\n')
        for pixel in row:
            brightness = (((0.21 * pixel[0]) + (0.72 * pixel[1]) + (0.07 * pixel[2])) / 3) / 3.95
            file.write("%s" % ascii_text[math.floor(brightness)] * 2)
