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

def polygon_area(polygon):
    """
    计算多边形的面积，支持非凸情况
    :param polygon: 多边形顶点，已经进行顺次逆时针排序
    :return: 该多边形的面积
    """
    n = len(polygon)
    if n < 3:
        return 0
    vectors = np.zeros((n, 2))
    for i in range(0, n):
        vectors[i, :] = polygon[i, :] - polygon[0, :]
    area = 0
    for i in range(1, n):
        v1, v2 = vectors[i-1, :], vectors[i, :]
        area = area + (v1[0]*v2[1] - v1[1]*v2[0]) / 2
    return abs(area)
 
def get_area(points):
    a, b, c, d = points
    max_size = (1000, 500)
    p = getCrossPoint([[a,b], [c,d]])
    # print(p)
    if max_size>p and p>(0,0):
        # print("wrong")
        area = polygon_area(np.array([a, c, b, d]))
        return area
    else:
        # print("yes")
        area = polygon_area(np.array([a, b, c, d]))
        return area

def get_max_quadrangle(points):
    if points is None:
        return None
    if len(points)<4:
        return None
    points = [i[0] for i in points]
    points = list(itertools.combinations(points, 4))
    points.sort(key=get_area, reverse=True)
    return points[0]
