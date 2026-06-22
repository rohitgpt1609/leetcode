class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n

        # Reverse entire array
        nums.reverse()

        # Reverse first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse remaining elements
        nums[k:] = reversed(nums[k:])