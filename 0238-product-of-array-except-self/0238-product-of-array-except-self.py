class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n

    # Step 1: Calculate prefix products
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

    # Step 2: Calculate suffix products on the fly
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]

        return res
