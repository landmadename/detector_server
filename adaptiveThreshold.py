import cv2

def canny(mat, ksize):
    gray = cv2.cvtColor(mat,cv2.COLOR_RGB2GRAY)
    gauss = cv2.GaussianBlur(gray, (ksize, ksize), 0.3*((ksize-1)*0.5-1)+0.8)
    edged = cv2.Canny(gauss, 75, 200)
    return edged
