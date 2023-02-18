import cv2
import numpy as np

if __name__ == '__main__':
    def callback(*arg):
        print(arg)

cv2.namedWindow("result")

cap = cv2.VideoCapture(0)

hsv_min = np.array((53, 55, 147), np.uint8)
hsv_max = np.array((83, 160, 255), np.uint8)

hsv2_min = np.array((53, 55, 147), np.uint8)
hsv2_max = np.array((83, 160, 255), np.uint8)

hsv3_min = np.array((53, 55, 147), np.uint8)
hsv3_max = np.array((83, 160, 255), np.uint8)

hsv4_min = np.array((53, 55, 147), np.uint8)
hsv4_max = np.array((83, 160, 255), np.uint8)

while True:
    flag, img = cap.read()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsv, hsv_min, hsv_max)
    thresh2 = cv2.inRange(hsv, hsv2_min, hsv2_max)
    thresh3 = cv2.inRange(hsv, hsv3_min, hsv3_max)
    thresh4 = cv2.inRange(hsv, hsv4_min, hsv4_max)

    moments = cv2.moments(thresh, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    moments = cv2.moments(thresh2, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    moments = cv2.moments(thresh3, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    moments = cv2.moments(thresh4, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']


    if dArea > 100:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
        print('green')

    cv2.imshow('result', img)

    ch = cv2.waitKey(5)
    if ch == 27:
        break

cap.release()
cv2.destroyAllWindows()


hsv_min = np.array((90, 70, 70), np.uint8)#голубой
hsv_max = np.array((150, 255, 255), np.uint8)
