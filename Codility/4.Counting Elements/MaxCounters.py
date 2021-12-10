def solution(N, A):
    counter = [0] * N
    for num in A:
        if num <= N:
            counter[num-1] += 1
        else:
            counter = [max(counter) for _ in counter]
    return counter

print(solution(5, [3,4,4,6,1,4,4]))