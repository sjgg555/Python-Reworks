import numpy as np
import math


def generate_sdf(image):
    """Per pixel, find the distance to the closest pixel with a specifed colour.
    Save the value to the pixel as greyscale"""
    target = np.array([255,255,255])
    output = image.copy()
    for x in range(0, image.height):
        for y in range(0, image.width):
            distance = get_distance_to_colour(x, y, image, target)
            output.setpixel(calculate_colour(distance))
    return output


def get_distance_to_colour(x, y, image, target):
    """spirals out from current pixel, return when the first pixel of colour is found"""       
    distance = -1
    spiral = get_spiral(image.width, image.height, x, y)
    for _ in range(image.width * image.height):
        x_t, y_t = next(spiral)
        x_prime = x + x_t 
        y_prime = y + y_t
        if (-1 < x_prime < image.width) and (-1 < y_prime < image.height):
            spiral_color = np.array(image.getpixel((x_prime, y_prime)))
        if np.equal(spiral_color, target):
            distance = math.floor(math.sqrt(x_t**2, y_t**2))
    return distance


def calculate_colour(distance):
    white = 255
    colour = white / distance 
    cutoff = 5
    return np.clip(colour, 0, cutoff)


def get_spiral(X_size, Y_size, x, y):
    dx = 0
    dy = -1
    x_size = 2 * X_size
    y_size = 2 * Y_size
    for _ in range(max(X_size, Y_size)**2):
        if (-x_size/2 < x <= x_size/2) and (-y_size/2 < y <= y_size/2):
            yield x, y
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
    return x, y