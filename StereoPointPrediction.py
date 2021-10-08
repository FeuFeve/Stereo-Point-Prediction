import cv2
import numpy as np
import os


# USER VARS

image_left = "TurtleG.tif"
image_right = "TurtleD.tif"
points_file_left = "TurtleG.txt"
points_file_right = "TurtleG.txt"


# GLOBAL VARS

images_directory = "images/"
points_directory = "points/"

img = None
cross_size = 6

points = []
point_counter = 0
nb_points = 0


# OPENCV DRAW FUNCTIONS

def draw_cross(x, y):
    global img, cross_size
    cv2.line(img, (x, y + cross_size), (x, y - cross_size), (0, 0, 255), 2)
    cv2.line(img, (x + cross_size, y), (x - cross_size, y), (0, 0, 255), 2)
    cv2.imshow('image', img)


# FUNCTIONS

def create_points_directory():
    exists = os.path.exists(points_directory)
    if not exists:
        os.makedirs(points_directory)


def points_file_exists(filename):
    return os.path.exists(points_directory + filename)


def click_event(event, x, y, flags, params):
    global points, point_counter
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        draw_cross(x, y)
        point_counter += 1
        print(f'Number of points: {point_counter}')


def save_to_points_file(filename):
    file = open(points_directory + filename, 'w')
    file.write('From image 1:\n')
    for p in points:
        file.write(f'{p[0]} {p[0]}\n')
    file.close()
    print(f'Saved to \'{points_directory + filename}\'')


def ask_user_to_draw_points_on(image_name, filename):
    global img
    img = cv2.imread(images_directory + image_name, cv2.IMREAD_COLOR)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', click_event)

    print('Click somewhere on the image to set a reference point, or press the \'f\' key to end input.')

    key = ''
    while key is not ord('f'):
        key = cv2.waitKey(0)

    print(f'User input ended with {point_counter} reference points.')
    print(f'Points list: {points}')
    save_to_points_file(filename)
    
    cv2.destroyAllWindows()


# MAIN

def main():
    create_points_directory()
    # if not points_file_exists(points_file_left): # TODO: Add back this line
    ask_user_to_draw_points_on(image_left, points_file_left)
    print("End of program.")


if __name__ == '__main__':
    main()
