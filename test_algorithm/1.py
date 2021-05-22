#实验是否可以跳格插入
nums1 = [1, 2, 3, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
nums1[m + n - 1] = nums2[n - 1]
print(nums1)