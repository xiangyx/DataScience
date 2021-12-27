from queue import PriorityQueue

def solution_v1(A):
    # write your code in Python 3.6
    half_of_sum = sum(A) * 0.5
    print(half_of_sum)
    reduced = 0
    count = 0
    while reduced < half_of_sum:
        A.sort()
        A[-1] /= 2
        reduced += A[-1]
        print(reduced)
        count =+ 1
    return count

def solution(A):
    half_of_sum = sum(A) * 0.5
    q = PriorityQueue()
    for num in A:
        q.put(0-num)
    reduced = 0
    count = 0
    while reduced < half_of_sum:
        pollution = 0-q.get()
        reduced += pollution * 0.5
        q.put(-pollution * 0.5)
        count += 1
    return count

print(solution([5, 19, 8, 1]))
print(solution([10, 10]))