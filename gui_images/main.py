# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:47:54 2021

@author: simon
"""

from dearpygui import core, simple
from PIL import Image
import os
import math
import numpy as np


def display_input_image(sender, data):
    file_path = os.path.join(data[0], data[1])
    core.log_info(file_path)
    core.set_value("file_name", data[1])
    
    with simple.window("Input Image", width=320, height=340):
        simple.set_window_pos("Input Image", 100, 300)
        
        core.add_drawing("##drawing_1", width=300, height=300)
        core.draw_image("##drawing_1", file_path, pmin=[0,0], pmax=[300, 300])
        
    display_output_sdf(file_path)
    

def calculate_colour(distance):
    white = 255
    colour = white / distance 
    cutoff = 5
    return np.clip(colour, 0, cutoff)


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


def display_output_sdf(file_path):
    """Takes an input image and outputs an sdf image,"""
    img = generate_sdf(Image.open(file_path).convert("LA"))
    
    dpg_image = []
    for i in range(0, img.height):
        for j in range(0, img.width):
            pixel = img.getpixel((j, i))
            dpg_image.append(pixel)
            dpg_image.append(pixel)
            dpg_image.append(pixel)
            dpg_image.append(255)
            
    with simple.window("Output Image", width=320, height=340):
        simple.set_window_pos("Output Image", 530, 300)
        
        #create a drawing to display the image
        core.add_drawing('##drawing_2', width=300, height=300)
        #create a texture to hold the image data
        core.add_texture("##texture", dpg_image, width=img.width, height=img.height)
        #draw the image data to the drawing
        core.draw_image("##drawing_2", "##texture", pmin=[0,0], pmax=[300, 300])


def pick_file(sender, data):
    core.open_file_dialog(callback=display_input_image, extensions=data)


def main():
    with simple.window("File", width=400, height=200):
        simple.set_window_pos("File", 300, 20)
        core.add_text("High Res-ify")
        core.add_text("File Path: ")
        core.add_same_line()
        core.add_text("##file_dir_text", default_value="None selected", source="file_name")
        core.add_button("Select File", callback=pick_file, callback_data=".png, .bmp, .jpg")
        
        core.set_main_window_size(1000, 1000)
        core.set_main_window_title("Python image processor")
        core.show_logger()
            
    core.start_dearpygui() 


if __name__ == "__main__":
    main()