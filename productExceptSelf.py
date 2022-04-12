# def productExceptSelf(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[int]
#     """
#     product = 1
#     zero_count = 0
#     zero_index = 0
    
#     for i,num in enumerate(nums):
#         if num == 0:
#             zero_count+=1
#             zero_index = i
#             if zero_count > 1:
#                 return [0] * len(nums)
#             else: 
#                 continue
#         product *= num;  

#     if zero_count == 1:
#         output = [0] * (len(nums) - 1)
#         output.insert(zero_index, product)
#         return output    
#     return [product/nums[i] for i in range(len(nums))]

def productExceptSelf(A):
        res = []
        prod = 1
        for a in A:
            res.append(prod)
            prod *= a
        print(res)
        prod = 1
        for i in range(len(A)-1, -1, -1):
            res[i] *= prod
            prod *= A[i]
        return res



# print(productExceptSelf([-1,1,5,-3,2]))


# for i in range(4,-1, -1):
#     print(i)

for i in range(1,1):
    print(i)
