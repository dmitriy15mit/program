import cv2
import numpy as np


camera = cv2.VideoCapture(0)

while True:

    flag, img = camera.read()
    low_blue = np.array((90, 70, 70), np.uint8)
    high_blue = np.array((150, 255, 255), np.uint8)

    try:

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    average_color_per_row = np.average(rgb, axis=0)
    average_color = np.average(average_color_per_row, axis=0)


    print("The color of the object is:")
    print("R:", int(average_color[0]), "G:", int(average_color[1]), "B:", int(average_color[2]))

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

search

