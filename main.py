import cv2
import numpy as np


img = cv2.imread('images/NY-rooftop.jpg', cv2.IMREAD_COLOR)
switch = False
p1, p2 = [], []


def draw_line(a, b, c):
    global img

    p1 = [0, int(round(-c/b))]

    height, width, channels = img.shape
    x2 = width - 1
    y2 = int(round(-(a * x2 + c) / b))
    p2 = [x2, y2]

    print(f'Drawing line from {p1} to {p2}')
    cv2.line(img, p1, p2, (0, 255, 0), 2)


def compute_line_coefs(p1, p2):
    global img
    a = (p2[1] - p1[1]) / (p2[0] - p1[0])
    b = (p1[1] - p1[0] * a)
    print(f'{a}x + {b}')

    v = [p2[0] - p1[0], p2[1] - p1[1]]
    alpha = v[1]
    beta = -v[0]
    gamma = -(alpha * p1[0] + beta * p1[1])

    print(f'{alpha}x + {beta}y + {gamma} = 0')

    draw_line(alpha, beta, gamma)
    cv2.imshow("image", img)
    


def click_event(event, x, y, flags, params):
    global switch, p1, p2
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'({x}, {y})')

        switch = not switch
        if switch:
            p1 = [x, y]
        else:
            p2 = [x, y]
            # cv2.line(img, p1, p2, (0, 0, 255), 2)
            cv2.imshow("image", img)
            compute_line_coefs(p1, p2)


def main():
    # a = np.array([
    #     [ 1, 2, 3],
    #     [ 4, 5, 6],
    #     [ 7, 8, 9]
    # ])
    # print(a)
    # a = a.transpose()
    # print(a)
    # b = np.linalg.inv(a)
    # print(b)
    # print(np.dot(a, b))
    x = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
    y = np.linalg.inv(x) 
    print(x)
    print(y)
    print(np.dot(x,y))

    cv2.imshow("image", img)
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite("images/NY-rooftop_modified.jpg", img)


if __name__ == '__main__':
    print("MAIN")
    main()
