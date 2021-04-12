# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:47:54 2021

@author: simon
"""

from dearpygui import core, simple
from PIL import Image
import os


def display_input_image(sender, data):
    file_path = os.path.join(data[0], data[1])
    core.log_info(file_path)
    core.set_value("file_name", data[1])
    
    with simple.window("Input Image", width=320, height=340):
        simple.set_window_pos("Input Image", 100, 300)
        
        core.add_drawing("##drawing_1", width=300, height=300)
        core.draw_image("##drawing_1", file_path, pmin=[0,0], pmax=[300, 300])
        
    display_output_sdf(file_path)


def display_output_sdf(file_path):
    """Takes an input image and outputs an sdf image,"""
    img = Image.open(file_path).convert("1")
    
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