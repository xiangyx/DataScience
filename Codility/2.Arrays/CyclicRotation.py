def solution(A, K):
    length = len(A)
    index_old = list(range(length))
    index_new = [(index_old[i] + K) % length for i in index_old]
    return [a for _, a in sorted(zip(index_new, A))]

print(solution([3,8,9,7,6], 3))

