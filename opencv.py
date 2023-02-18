import cv2

import numpy as np

if __name__ ==  '__main__':
    def nothing(*arg):
        pass

    cv2.namedWindow( 'out_window')
    cap = cv2.VideoCapture(0)

    while True:
        flag, img = cap.read()

        low_blue = np.array((90,70,70), np.uint8)
        high_blue = np.array((150,255,255), np.uint8)
        try:
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            mask_blue = cv2.inRange(img_hsv, low_blue, high_blue)

            cv2.imshow('out window', mask_blue)
        except:
            cap.release()
            raise
        k = cv2.waitKey(30) & 0xFF
        if k == 27:
            break
cap.release()
cv2.destroyAllWindows()


