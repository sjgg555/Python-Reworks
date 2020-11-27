# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 17:29:54 2020

@author: simon
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from scipy.spatial.transform import Rotation as R


def normalise(vector):
    return vector / np.sqrt(vector[0]**2 + vector[1]**2 + vector[2]**2)


def plot_points(xs, ys, zs):
    fig = plt.figure(figsize=(10,8), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(xs, ys, zs)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    ax.set_zlim(-20, 20)

    plt.show()  


def rotate(points, normal_vector, angle):
    r = R.from_rotvec(np.radians(angle) * np.array(normalise(normal_vector)))
    r.as_matrix()
    return r.apply(points.T).T


def create_circle(centre, start_angle, end_angle, radius, point_count):
    angles = np.linspace(start_angle, end_angle, point_count, endpoint=False)
    
    x_coords = centre[0] + (radius * np.cos(angles))
    y_coords = centre[1] + (radius * np.sin(angles))
    z_coords = centre[2] + np.zeros(point_count)
    
    return np.array([x_coords, y_coords, z_coords])


def create_spiral(centre, start_angle, end_angle, radius, length, revolutions, points_per_rev):
    angles = np.linspace(start_angle, revolutions * end_angle, points_per_rev * revolutions, endpoint=False)
    lengths = np.linspace(-length/2, length/2, points_per_rev * revolutions, endpoint=False)
    
    x_coords = centre[0] + (radius * np.cos(angles))
    y_coords = centre[1] + (radius * np.sin(angles))
    z_coords = centre[2] + lengths
    
    return np.array([x_coords, y_coords, z_coords])
    

def main():
    # circle
    start = 0
    end = 2 * np.pi
    point_count = 100
    radius = 10
    centre = 0.,0.,0.
    normal = 0.,1.,0.
    rotation_angle = 10
    coords = create_circle(centre, start, end, radius, point_count)
    coords = rotate(coords, normal, rotation_angle)
    plot_points(*coords)
    
    # spiral
    start = 0
    end = 2 * np.pi
    points_per_rev = 100
    radius = 10
    length = 40
    revolutions = 3
    
    centre = 0.,0.,0.
    normal = 1.,1.,1.
    rotation_angle = 10
    coords = create_spiral(centre, start, end, radius, length, revolutions, points_per_rev)
    coords = rotate(coords, normal, rotation_angle)
    plot_points(*coords)


if __name__ == "__main__":
    main()
