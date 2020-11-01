#!/usr/bin/env python

# import cv2.cv2 as cv2
# import imutils
# import numpy as np
# from imutils.video import VideoStream
from tkinter import *

# create blank window
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry("500x500")
# label = Label(window, "hello")
haiding=Label(text="OpenCV GameController")
haiding.pack()
button = Button(window,text = "Run",command = "myFun" )
button.pack()  



window.mainloop()

# video = VideoStream(src=0).start()
# frame = None

# lb = [40, 100, 0]
# rb = [255, 255, 255]



# cv2.namedWindow('mask')

# def process_wheel():
    
#     global frame
#     wheel_frame = frame.copy()

#     hsv = cv2.cvtColor(wheel_frame, cv2.COLOR_BGR2HSV)

#     lower_blue = np.array(lb.copy())  # [35, 100, 0]
#     upper_blue = np.array(rb.copy())  # [255, 255, 255])

#     mask = cv2.inRange(hsv, lower_blue, upper_blue)

#     anded_res = cv2.bitwise_and(wheel_frame, wheel_frame, mask=mask)
#     contours, _ = cv2.findContours(cv2.Canny(anded_res, 255 / 3, 255), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     # print(contours)
#     area_threshold = 400
#     inds = []
#     for i, c in enumerate(contours):
#         a = cv2.contourArea(c)
#         if a > area_threshold and len(inds) < 2:
#             inds.append(i)

#     if not inds or len(inds) != 2:
#         cv2.imshow('wheel', wheel_frame)  # [165:200, 326:500])
#         cv2.imshow('mask', mask)  # [165:200, 326:500])
#         return

#     if cv2.contourArea(contours[inds[0]]) < cv2.contourArea(contours[inds[1]]):
#         inds[0], inds[1] = inds[1], inds[0]

#     moments1 = cv2.moments(contours[inds[0]])
#     moments2 = cv2.moments(contours[inds[1]])

#     p1 = [int(moments1["m10"] / moments1["m00"]), int(moments1["m01"] / moments1["m00"])]
#     p2 = [int(moments2["m10"] / moments2["m00"]), int(moments2["m01"] / moments2["m00"])]


#     cv2.circle(wheel_frame, (p1[0], p1[1]), 3, (255, 255, 255), -1)
#     cv2.circle(wheel_frame, (p2[0], p2[1]), 3, (255, 255, 255), -1)

#     cv2.line(wheel_frame, (p1[0], p1[1]), (p2[0], p2[1]), (0, 0, 0), 2)
#     if p2[0] - p1[0] == 0:
#         slope = 90
#     else:
#         slope = -np.rad2deg(np.arctan2((p2[1] - p1[1]), (p2[0] - p1[0]))) % 360

#     cv2.drawContours(wheel_frame, contours, inds[0], (0, 0, 255), 2)
#     cv2.drawContours(wheel_frame, contours, inds[1], (0, 255, 0), 2)

#     cv2.putText(wheel_frame, "Angle: {}".format(np.round(slope)), (5, 60), cv2.FONT_HERSHEY_PLAIN, 1,
#                 (0, 0, 255), 1 )

#     cv2.putText(wheel_frame, "{}".format("{} {}".format(p2, p1)), (5, 90), cv2.FONT_HERSHEY_PLAIN,1,
#                 (0, 0, 255), 1)

#     cv2.line(wheel_frame, (0, 200), (600, 200), (0, 0, 0), 1)
#     cv2.line(wheel_frame, (0, 250), (600, 250), (0, 0, 0), 1)
#     # steer(slope)
#     # gas(p1[1])
#     cv2.imshow('wheel', wheel_frame)  # [165:200, 326:500])
#     cv2.imshow('mask', mask)  # [165:200, 326:500])


# while True:
#     # Capture frame-by-frame
#     frame = video.read()

#     frame = cv2.flip(frame, 1)
#     # frame = cv2.medianBlur(frame, 5)
#     frame = imutils.resize(frame, width=600, height=400)

#     process_wheel()

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # When everything done, release the capture
# video.stop()
# cv2.destroyAllWindows()
