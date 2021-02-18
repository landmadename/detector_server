import cv2
import json
from adaptiveThreshold import canny
from Countours import Countours
from approxPoly import approxPoly
from HoughLines import draw_mask
from Harris import Harris
from resize import resize
from draw_corners import draw_corners
from get_max_quadrangle import get_max_quadrangle


ksize = 5
epsilon = 13
pre_quadrangle = None

max_size = (1000, 500)

width = int(1920/3)
height = int(1080/3)

def format_points(points):
    points = points[::-1]
    points = [{"x": i[0], "y": i[1]} for i in points]
    points = json.dumps(points)
    return points

def do(mat):
    mat = resize(mat, max_size)
    raw = mat.copy() 
    twoValue = canny(mat, ksize)
    cnts = Countours(twoValue)
    mat = approxPoly(twoValue, cnts, epsilon)

    mask = draw_mask(mat)
    corners = Harris(mat,mask)
    quadrangle = get_max_quadrangle(corners)
    # raw = draw_corners(raw, quadrangle)
    # cv2.imshow('img', raw)
    # cv2.imwrite("./imgs/out.png",raw)
    return quadrangle

def detect_pic():
    filename = "./imgs/file.png"
    mat = cv2.imread(filename)
    points = format_points(do(mat))
    return points