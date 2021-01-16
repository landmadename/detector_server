import numpy as np
import itertools

import math

#Graham扫描法
#获取基准点的下标,基准点是p[k]
def get_leftbottompoint(p):
    k = 0
    for i in range(1, len(p)):
        if p[i][1] < p[k][1] or (p[i][1] == p[k][1] and p[i][0] < p[k][0]):
            k = i
    return k

#叉乘计算方法
def multiply(p1, p2, p0):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])

#获取极角，通过求反正切得出，考虑pi/2的情况
def get_arc(p1, p0):
    # 兼容sort_points_tan的考虑
    if (p1[0] - p0[0]) == 0:
        if ((p1[1] - p0[1])) == 0:
            return -1;
        else:
            return math.pi / 2
    tan = float((p1[1] - p0[1])) / float((p1[0] - p0[0]))
    arc = math.atan(tan)
    if arc >= 0:
        return arc
    else:
        return math.pi + arc

#对极角进行排序,排序结果list不包含基准点
def sort_points_tan(p, pk):
    p2 = []
    for i in range(0, len(p)):
        p2.append({"index": i, "arc": get_arc(p[i], pk)})
    #print('排序前:',p2)
    p2.sort(key=lambda k: (k.get('arc')))
    #print('排序后:',p2)
    p_out = []
    for i in range(0, len(p2)):
        p_out.append(p[p2[i]["index"]])
    return p_out

def convex_hull(p):
    p=list(set(p))
    #print('全部点:',p)
    k = get_leftbottompoint(p)
    pk = p[k]
    p.remove(p[k])
    #print('排序前去除基准点的所有点:',p,'基准点:',pk)

    p_sort = sort_points_tan(p, pk)   #按与基准点连线和x轴正向的夹角排序后的点坐标
    #print('其余点与基准点夹角排序:',p_sort)
    p_result = [pk,p_sort[0]]

    top = 2
    for i in range(1, len(p_sort)):
        #####################################
        #叉乘为正,向前递归删点;叉乘为负,序列追加新点
        while(multiply(p_result[-2], p_sort[i],p_result[-1]) > 0):
            p_result.pop()
        p_result.append(p_sort[i])    
    return p_result#测试

def GetAreaOfPolyGonbyVector(points):
    # 基于向量叉乘计算多边形面积
    area = 0
    if(len(points)<3):
        raise Exception("error")

    for i in range(0,len(points)-1):
        p1 = points[i]
        p2 = points[i + 1]

        triArea = (p1[0]*p2[1] - p2[0]*p1[1])/2
        #print(triArea)
        area += triArea

    fn=(points[-1][0]*points[0][1]-points[0][0]*points[-1][1])/2
    #print(fn)
    return abs(area+fn)


def get_max_quadrangle(points):
    if points is None:
        return None
    if len(points)<4:
        return None
    points = points.tolist()
    points = [(i[0][0], i[0][1]) for i in points]
    points = list(itertools.combinations(points, 4))
    points = [convex_hull(i) for i in points]
    points.sort(key=GetAreaOfPolyGonbyVector, reverse=True)
    return points[0]
