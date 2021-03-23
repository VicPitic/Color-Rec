import cv2
import os
import numpy as np
import time
import face_recognition
import pyautogui


cap = cv2.VideoCapture(0)

yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])

red_lower = np.array([0, 120, 70])
red_upper = np.array([10, 255, 255])

prev_y = 0

while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, red_lower, red_upper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c)
        if area > 3000:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 4)
            print(y)

            """
            if(y < prev_y):
                print("Scroll Down")
                pyautogui.scroll(-100)
            else:
                print("Scroll Up")
                pyautogui.scroll(100)
            """

            if(y > 400):
                pyautogui.scroll(-100)
            elif(y < 200):
                pyautogui.scroll(100)

            prev_y = y

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    if cv2.waitKey(10) == ord("q"):
        break

cap.read()
cv2.destroyAllWindows()