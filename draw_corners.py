import numpy as np
import cv2

def draw_corners(raw, corners):
    if corners is None:
        return raw
    corners = np.int0(corners)
    for i in corners:
        x,y = i.ravel()
        cv2.circle(raw,(x,y),15,(0,255,0),-1)
    return raw