def solution_v1(A):
    for num in A:
        if A.count(num) != 1:
            A.remove(num)
            A.remove(num)
    return A[0]

def solution_v2(A):
    unique_elements = list(set(A))
    for num in unique_elements:
        if A.count(num) % 2 == 1:
            return num

def solution(A):
    dict_count = {}
    for num in A:
        if num not in dict_count:
            dict_count[num] = 1
        else:
            dict_count[num] += 1
    for num in dict_count:
        if dict_count[num] % 2 == 1:
            return num
            
def solution_v3(A):
    unique_set = set()
    for num in A:
        if num not in unique_set:
            unique_set.add(num)
        else:
            unique_set.remove(num)
    return unique_set.pop()