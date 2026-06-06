# Kth Largest Element in Array

## Problem Statement
Given an integer array `nums` and an integer `k`, return the kth largest element in the array. The array can contain duplicate elements and the kth largest element is defined as the kth element in the sorted array in descending order, i.e., the kth element from the end in the sorted array. For example, if the input array is `[3, 2, 1, 5, 6, 4]` and `k = 2`, the output should be `5`. The constraints are `1 <= k <= nums.size()` and the array can contain any integer values.

## Approach
The approach to solve this problem is to use the QuickSelect algorithm, which is a variant of the QuickSort algorithm. This algorithm works by selecting a pivot element, partitioning the array around the pivot, and then recursively searching for the kth largest element in the appropriate partition. The algorithm has an average time complexity of O(n), making it efficient for large inputs.

## Complexity
- Time: O(n) on average, O(n^2) in the worst case
- Space: O(1) for the auxiliary space used by the QuickSelect algorithm

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // Call the QuickSelect function to find the kth largest element
        return quickSelect(nums, 0, nums.size() - 1, nums.size() - k);
    }

    int quickSelect(vector<int>& nums, int left, int right, int k) {
        // If the list contains only one element, return that element
        if (left == right) {
            return nums[left];
        }

        // Select a pivot index
        int pivotIndex = partition(nums, left, right);

        // If the pivot is at the kth position, return the pivot
        if (k == pivotIndex) {
            return nums[k];
        }
        // If the kth position is on the left side of the pivot, recurse on the left side
        else if (k < pivotIndex) {
            return quickSelect(nums, left, pivotIndex - 1, k);
        }
        // If the kth position is on the right side of the pivot, recurse on the right side
        else {
            return quickSelect(nums, pivotIndex + 1, right, k);
        }
    }

    int partition(vector<int>& nums, int left, int right) {
        // Choose the middle element as the pivot
        int pivot = nums[(left + right) / 2];

        // Move all elements smaller than the pivot to the left and all elements larger to the right
        int i = left;
        int j = right;
        while (i <= j) {
            while (nums[i] < pivot) {
                i++;
            }
            while (nums[j] > pivot) {
                j--;
            }
            if (i <= j) {
                swap(nums[i], nums[j]);
                i++;
                j--;
            }
        }

        // Return the final index of the pivot
        return i - 1;
    }
};
```

## Test Cases
```
Input: nums = [3, 2, 1, 5, 6, 4], k = 2
Output: 5
Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
Output: 4
```

## Key Takeaways
- The QuickSelect algorithm is a variant of the QuickSort algorithm that can be used to find the kth smallest or largest element in an array.
- The average time complexity of the QuickSelect algorithm is O(n), making it efficient for large inputs.
- The worst-case time complexity of the QuickSelect algorithm is O(n^2), which can occur if the pivot is chosen poorly.