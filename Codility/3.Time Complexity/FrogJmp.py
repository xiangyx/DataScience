import math

def solution(X, Y, D):
    num_step = (Y - X) / D
    return math.ceil(num_step)

print(solution(10, 85, 30))