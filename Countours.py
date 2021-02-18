import cv2

def Countours(mat):
    cnts = cv2.findContours(mat, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    return cnts[1:]
