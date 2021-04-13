# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 12:51:00 2021

@author: simon
"""

import main as _sut
from PIL import Image
import pytest
import numpy as np

class TestClass:
    
    WHITE = [255, 255, 255]
    BLACK = [0, 0, 0]    
    
    def test_spiral_2x2(self):
        x_size = 2
        y_size = 2
        x = 0
        y = 0
        spiral = _sut.get_spiral(x_size, y_size, x, y)
        expected = np.array([(0,0), (1,0), (1,1), (0,1)])
        for i, result in enumerate(spiral):
            assert all(np.equal(np.array(result), np.array(expected[i])))


    def test_spiral_2x2_from_1x1(self):
        x_size = 2
        y_size = 2
        x = 1
        y = 1
        spiral = _sut.get_spiral(x_size, y_size, x, y)
        expected = np.array([(1,1), (2,1), (2,2), (1,2)])
        for i, result in enumerate(spiral):
            assert all(np.equal(np.array(result), np.array(expected[i])))



    def test_distance(self):
        im = Image.open("Y:\\Code Projects\\Python-Reworks\\gui_images\\test_images\\20x20_dot.png").convert("LA")
        results = _sut.get_distance_to_colour(1, 1, im, self.WHITE)
        print(results)

        
    def test_get_dist(self):
        im = Image.open("Y:\\Code Projects\\Python-Reworks\\gui_images\\test_images\\20x20_dot.png").convert("LA")
        result = _sut.get_distance_to_colour(1, 1, im, self.WHITE)
        assert result == 1


if __name__ == "__main__":
    tests = TestClass()
    tests.test_spiral_2x2()
    tests.test_spiral_2x2_from_1x1()
    tests.test_get_dist()
