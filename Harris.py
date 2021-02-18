import cv2

def Harris(img, mask):
    corners = cv2.goodFeaturesToTrack(
        image=img,
        maxCorners=20,
        qualityLevel=0.06,
        minDistance=100,
        mask=mask,
        blockSize=3,
        useHarrisDetector=True)
    return corners
