import cv2
import numpy as np
cap=cv2.VideoCapture('nobita.mp4')

while cap.isOpened():
    sucess,frame=cap.read()
    if sucess:
        zeros=np.zeros((frame.shape[0],frame.shape[1]),np.uint8)
        b,g,r=cv2.split(frame)

        blue=cv2.merge([b,zeros,zeros])
        green=cv2.merge([zeros,g,zeros])
        red=cv2.merge([zeros,zeros,r])
        custom_image = cv2.merge([b, g, r])
        gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.imshow('Blue',blue)
        cv2.imshow('Green',green)
        cv2.imshow('Red',red)
        cv2.imshow('Frame',frame)
        cv2.imshow('Custom Image',custom_image)
        cv2.imshow('GrayScale Image',gray_image)
        k=cv2.waitKey(50)

        if k & 0xff==ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()