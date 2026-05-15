import sys

def get_path(n, m):
    path = []
    current = 1
    while True:
        path.append(current)
        current = (current + m - 2) % n + 1
        if current == 1:
            break
    return ''.join(map(str, path))

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python task1.py n1 m1 n2 m2")
        sys.exit(1)
    
    n1, m1 = int(sys.argv[1]), int(sys.argv[2])
    n2, m2 = int(sys.argv[3]), int(sys.argv[4])
    
    result = get_path(n1, m1) + get_path(n2, m2)
    print(result)
