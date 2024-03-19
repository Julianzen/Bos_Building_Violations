# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:16:46 2024

@author: julia
"""


import copy
import math

"""
This section below is for reading the polygons.txt file to get the neighborhood coordinates.
Then turning the txt file's material into an array based on neighborhoods.
So for example Roxbury would be [....[[Roxbury],[x1,y1],[x2,y2],...[xi,yi]]]

Where each row like poly[0] would be the coodrinates for Beacon Hill with poly[0][0] being:
[Beacon Hill] and poly[0][1...i] and onwards will be [xi,yi] coordinates

"""
poly = [[]]*22

for i in range(len(poly)):
    poly[i] = copy.deepcopy([i])
    


f = open("polygons.txt", "r")

st = f.read()
lines = st.strip().split('\n')

lin = []

for i in lines:
    a = i.strip(" ")
    z = a.split(",")
    lin.append(z)

s = 0
j = 0

for i in range(0,len(lin)):
   if len(lin[i]) != 1:
       poly[j].append(lin[i])
   if len(lin[i]) == 1 and s == 1:
       j += 1
       poly[j][0] = lin[i]
   
   if s == 0:
       poly[j][0] = lin[i]
       s = 1

"""

Flips the coordinates of the neighborhood polygon 
since x and y are flipped in the orignal file

"""
for i in range(len(poly)):
    for j in range(len(poly[i])):
        if len(poly[i][j]) == 2:
            a = float(poly[i][j][1])
            b = float(poly[i][j][0])
            poly[i][j][0] = a
            poly[i][j][1] = b


"""
Method for finding distance

"""
def dist(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

"""

Method for finding polygon collisions with a point.

Also finds the closest distance between a point and one of the polygon's point
in case the point is not in any of the neighborhoods, so it can give the closest match with
a caveat of max distance of 0.0053561646726054

"""

def collider(point, vs):
    x = point[0]
    y = point[1]
    inside = False
    j = len(vs) - 1
    closestdistance = float('inf')
    for i in range(len(vs)):
        xi = vs[i][0]
        yi = vs[i][1]
        xj = vs[j][0]
        yj = vs[j][1]
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
        j = i
        distance1 = dist(point, vs[i])
        distance2 = dist(point, vs[j])
        if closestdistance > distance1:
            closestdistance = distance1
        if closestdistance > distance2:
            closestdistance = distance2
        
    return inside, closestdistance


def checkNeighborhood(point):
    inany = False
    closestdistance = float('inf')
    closestneighbor = float('inf')
    for i in range(len(poly)):
        tempray = copy.deepcopy(poly[i])
        head = tempray.pop(0)
        inside, distance = collider(pointy, tempray)
        if inside == True:
            print("In "+head[0])
            inany = True
        else:
            if closestdistance > distance:
                closestdistance = distance
                closestneighbor = head[0]
            
    if inany == False:
        print(closestdistance)
        print(closestneighbor)
        
    
    

    

pointy = [42.33893, -71.07194]
checkNeighborhood(pointy)
    
    

    




    
        

    
    

    
                
                
        
            
            
            
            
            
            


