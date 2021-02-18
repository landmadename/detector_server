import cv2
import numpy as np


def approxPoly(mat, cnts, epsilon):
    mat = np.zeros_like(mat)
    for c in cnts:
        if cv2.arcLength(c,True) > 50:
            approx = cv2.approxPolyDP(c, epsilon, True)
            cv2.polylines(mat, [approx], True, 255, 1, cv2.LINE_8)
    return mat