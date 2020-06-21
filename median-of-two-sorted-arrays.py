"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.
Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))


def findMedianSortedArrays(param_1, param_2):
    param_1.extend(param_2)
    param_1.sort()
    if len(param_1) % 2:
        return param_1[int(len(param_1) / 2)]
    else:
        return (param_1[int(len(param_1) / 2) - 1] + param_1[int(len(param_1) / 2)]) / 2


print(findMedianSortedArrays(list1, list2))
