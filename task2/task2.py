import sys

def point_relative_to_ellipse(cx, cy, rx, ry, x, y):
    value = ((x - cx) ** 2) / (rx ** 2) + ((y - cy) ** 2) / (ry ** 2)
    if abs(value - 1.0) < 1e-10:
        return 0
    elif value < 1:
        return 1
    else:
        return 2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python task2.py <ellipse_file> <points_file>")
        sys.exit(1)
    
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]
    
    with open(ellipse_file, 'r') as f:
        cx, cy = map(float, f.readline().split())
        rx, ry = map(float, f.readline().split())
    
    with open(points_file, 'r') as f:
        points = [list(map(float, line.split())) for line in f if line.strip()]
    
    for x, y in points:
        print(point_relative_to_ellipse(cx, cy, rx, ry, x, y))
