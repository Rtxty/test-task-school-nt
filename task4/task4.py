import sys

def min_moves_to_equal(nums):
    nums_sorted = sorted(nums)
    median = nums_sorted[len(nums_sorted) // 2]
    return sum(abs(x - median) for x in nums)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task4.py <file_with_numbers>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    with open(file_path, 'r') as f:
        nums = [int(line.strip()) for line in f if line.strip()]
    
    moves = min_moves_to_equal(nums)
    
    if moves <= 20:
        print(moves)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
