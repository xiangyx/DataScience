def decimal_to_binary(n):
    binary = ''
    while n != 0:
        binary += str(n % 2)
        n = int(n / 2)
    return binary[::-1]

def solution(n):
    binary_n = list(decimal_to_binary(n))
    if '0' not in binary_n:
        return 0
    elif binary_n.count('1') == 1:
        return 0
    else:
        first_1 = 0
        max_length = 0
        for index, value in enumerate(binary_n):
            if value == '1':
                max_length = max(max_length, index - first_1 - 1)
                first_1 = index
        return max_length

n = 529
a = [-5, -3, -1, 0, 1, 3, 5]
print(decimal_to_binary(n))
print(solution(n))
    