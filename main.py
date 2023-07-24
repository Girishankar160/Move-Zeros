def move_zeros(nums):
    n = len(nums)
    left = 0
    right = 0

    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
nums1 = [0, 1, 0, 3, 12]
move_zeros(nums1)
print(nums1)

nums2 = [0]
move_zeros(nums2)
print(nums2)