import cv2

def process(mat, a, b):
    grayImage  = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)
    gaussImage = cv2.GaussianBlur(grayImage, (5, 5), 0)
    edgedImage = cv2.Canny(gaussImage, a, b, apertureSize=3)
    return edgedImage