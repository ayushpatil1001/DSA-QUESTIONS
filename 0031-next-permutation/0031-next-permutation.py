
class Solution:
    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 2

        # Step 1: Find the first smaller number from right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: Find a number greater than nums[i]
        if i >= 0:
            j = n - 1

            while nums[j] <= nums[i]:
                j -= 1

            # Step 3: Swap the numbers
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the remaining part
        left = i + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
