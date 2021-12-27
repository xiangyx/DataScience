def solution(N, K):
    nums = [int(i) for i in str(N)]
    for i in range(len(nums)):
        if K == 0:
            break
        else:
            increase = 9-nums[i] if (9-nums[i] <= K) else K
            nums[i] = nums[i]+increase
            K = K - increase
    convertDigitsToInt = lambda nums: int(''.join(str(i) for i in nums))
    return convertDigitsToInt(nums)

    
