import cv2

def resize(mat, max_size):
    x, y = mat.shape[0:2]
    mx, my = max_size
    rx = x/mx
    ry = y/my

    if max([rx,ry]) > 1:
        ratio = max([rx,ry])
        return cv2.resize(mat, (int(y/ratio), int(x/ratio)))
    else:
        return mat