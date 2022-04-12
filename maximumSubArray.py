
# iterative approach
def maxSubArrayiter(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    if len(nums) == 1:
        return nums[0]
     
    subSum = nums[0]
    maxSum = subSum
    print("maxSum: ", maxSum)
    for i in range(1,len(nums)):
        num = nums[i]
        if num >= (num + subSum):
            subSum = num
        else: subSum += num
        maxSum = max(num, subSum, maxSum)
    return maxSum

print(maxSubArrayiter([-2,1,-3,4,-1,2,1,-5,4]))

# # devide and conquer

# def maxSubArrayRecur(nums):
#     if (len(nums) == 1):
#         return nums[0]
    
#     maxSubExcludeFirst = maxSubArrayRecur(nums[1:])

#     maxSum = nums[0]
#     curSum = nums[0]

#     for i in range(1, len(nums)):
#         curSum+= nums[i]
#         if curSum 


    



#     return max(, findMaxSumFromStart(nums))


        