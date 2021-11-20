from PIL import Image
import numpy as np


img = Image.open('img2.jpg')


def get_image(image, image_size=10, gradation=50):
    threshold = 255 // gradation
    width = len(image)
    height = len(image[0])
    x = 0
    while x < width:
        y = 0
        while y < height:
            sector = image[x: x + image_size, y: y + image_size]
            sum_avg = np.sum(sector) / 3
            average_color = int(sum_avg // (image_size * image_size))
            set_color(int(average_color // threshold) * threshold, image, image_size, x, y)
            y += image_size
        x += image_size
    return Image.fromarray(np.uint8(image))


def set_color(new_color, image, image_size, x, y):
    for r in range(x, x + image_size):
        for g in range(y, y + image_size):
            for b in range(3):
                image[r][g][b] = new_color


image_arr = np.array(img).astype(int)
get_image(image_arr).save('res.jpg')
