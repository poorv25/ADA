import math

def distance(p1, p2):
    """
    Computes the Euclidean distance between two points in 2D space.
    """
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def brute_force_closest_pair(points):
    """
    Finds the closest pair of points in the given list using a brute-force algorithm.
    """
    min_distance = float('inf')
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            d = distance(points[i], points[j])
            if d < min_distance:
                min_distance = d
                closest_pair = (points[i], points[j])
    return closest_pair

def closest_pair(points):
    """
    Finds the closest pair of points in the given list using a divide-and-conquer algorithm.
    """
    n = len(points)
    if n <= 3:
        return brute_force_closest_pair(points)
    
    mid = n // 2
    left = points[:mid]
    right = points[mid:]
    
    closest_pair_left = closest_pair(left)
    closest_pair_right = closest_pair(right)
    
    if distance(*closest_pair_left) < distance(*closest_pair_right):
        closest_pair = closest_pair_left
        min_distance = distance(*closest_pair_left)
    else:
        closest_pair = closest_pair_right
        min_distance = distance(*closest_pair_right)
        
    strip = [p for p in points if abs(p[0] - points[mid][0]) < min_distance]
    strip.sort(key=lambda p: p[1])
    
    for i in range(len(strip)-1):
        for j in range(i+1, min(i+7, len(strip))):
            d = distance(strip[i], strip[j])
            if d < min_distance:
                min_distance = d
                closest_pair = (strip[i], strip[j])
                
    return closest_pair
