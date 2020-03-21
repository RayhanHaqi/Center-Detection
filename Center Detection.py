import cv2 as cv
import numpy as np
def nothing(x):
    pass

vid = cv.VideoCapture(0)
cv.namedWindow('niggs')
cv.resizeWindow('niggs', 400,300)
cv.createTrackbar('hl', 'niggs', 0, 179, nothing)
cv.createTrackbar('sl', 'niggs', 0, 255, nothing)
cv.createTrackbar('vl', 'niggs', 0, 255, nothing)
cv.createTrackbar('hu', 'niggs', 179, 179, nothing)
cv.createTrackbar('su', 'niggs', 255, 255, nothing)
cv.createTrackbar('vu', 'niggs', 255, 255, nothing)

while(True):
    ret, frame = vid.read()
    (a, b) = frame.shape[:2]
    frame2 = cv.cvtColor(frame, cv.COLOR_BGR2HSV)	
    h_l = cv.getTrackbarPos('hl', 'niggs')	
    s_l = cv.getTrackbarPos('sl', 'niggs')	
    v_l = cv.getTrackbarPos('vl', 'niggs')	
    h_u = cv.getTrackbarPos('hu', 'niggs')	
    s_u = cv.getTrackbarPos('su', 'niggs')	
    v_u = cv.getTrackbarPos('vu', 'niggs')
    
    frame3 = cv.inRange(frame2, (h_l, s_l, v_l), (h_u, s_u, v_u))

    mask = cv.bitwise_and(frame2, frame2, mask = frame3)
    frame4 = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    frame5 = cv.GaussianBlur(frame4, (5,5), cv.BORDER_DEFAULT)
	
    ret2, thresh = cv.threshold(frame5, 0, 255, cv.THRESH_BINARY_INV)
	
    
    cv.imshow('lol', thresh)

    cv.circle(frame, (int(b/2), int(a/2)), 20, (0, 0, 255), 2)
    #cv.circle(frame, (b/2-20, a/2), 1, (255,0,0), 5)
    #cv.circle(frame, (b/2+20, a/2), 1, (255,0,0), 5)
    #cv.circle(frame, (b/2, a/2-20), 1, (255,0,0), 5)
    #cv.circle(frame, (b/2, a/2+20), 1, (255,0,0), 5)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        if cv.contourArea(cnt) > 4000:
            cv.drawContours(frame, cnt, -1, (255, 0, 0), 2)
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            x1 = x + int(w/2)
            y1 = y + int(h/2)
            cv.circle(frame, (x1, y1), 1, (255, 0, 0), 5)
            if x1 > int(b/2)-20 and x1 < int(b/2)+20 and y1 > int(a/2)-20 and y1 < int(a/2)+20:
                cv.putText(frame, "Centered (" + str(x1) + ", " + str(y1) + ")", (200,50), cv.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 2)
            
    cv.imshow('niggs1', frame)

    k = cv.waitKey(1)
    if k == 27:
        break