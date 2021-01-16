import cv2
import numpy as np
import itertools

def getLinePara(line):
    '''简化交点计算公式'''
    a = line[0][1] - line[1][1]
    b = line[1][0] - line[0][0]
    c = line[0][0] *line[1][1] - line[1][0] * line[0][1]
    return a,b,c

def getCrossPoint(lines):
    '''计算交点坐标，此函数求的是line1中被line2所切割而得到的点，不含端点'''
    line1,line2 = lines
    a1,b1,c1 = getLinePara(line1)
    a2,b2,c2 = getLinePara(line2)
    d = a1* b2 - a2 * b1
    p = [0,0]
    if d == 0:#d为0即line1和line2平行
        return ()
    else:
        p[0] = int((b1 * c2 - b2 * c1)*1.0 / d)
        p[1] = int((c1 * a2 - c2 * a1)*1.0 / d)
    p = tuple(p)
    return p

def convert_line(line):
    rho, theta = line
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    return ((x1,y1), (x2,y2))

def get_distance_from_point_to_line(lines):
    line1, line2 = lines
    point = line1[0]
    line_point1, line_point2 = line2
	#计算直线的三个参数
    A = line_point2[1] - line_point1[1]
    B = line_point1[0] - line_point2[0]
    C = (line_point1[1] - line_point2[1]) * line_point1[0] + \
        (line_point2[0] - line_point1[0]) * line_point1[1]
    #根据点到直线的距离公式计算距离
    distance = np.abs(A * point[0] + B * point[1] + C) / (np.sqrt(A**2 + B**2)+1e-6)
    return distance

def draw_mask(mat):
    edgedImage = cv2.Canny(mat, 30,250,apertureSize=3)
    lines = cv2.HoughLines(edgedImage,1,np.pi/180,80)
    mask = np.zeros_like(mat)
    
    if lines is None:
        return mask
    
    lines = [convert_line(line[0]) for line in lines]
    lines = itertools.combinations(lines, 2)
    lines = [i for i in lines if get_distance_from_point_to_line(i)>1000]
    points = [getCrossPoint(i) for i in lines]
    for point in points:
        if point != ():
            cv2.circle(mask,point,15,255,-1)
    return mask
