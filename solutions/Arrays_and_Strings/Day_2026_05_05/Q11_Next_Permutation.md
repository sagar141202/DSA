# Next Permutation

## Problem Statement
Given an array of integers, find the next lexicographically greater permutation of the array. If no such permutation exists, the function should return the first permutation (i.e., the array sorted in ascending order). For example, given the array [1, 2, 3], the next permutation is [1, 3, 2]. The array is 1-indexed and does not contain duplicate elements. The length of the array is between 1 and 100.

## Approach
The algorithm works by finding the first decreasing element from the right, then finding the smallest element greater than it on the right side, and swapping them. The elements on the right side are then reversed to get the next permutation.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        // Find the first decreasing element from the right
        int i = nums.size() - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        
        // If no decreasing element is found, the array is the last permutation
        if (i >= 0) {
            // Find the smallest element greater than nums[i] on the right side
            int j = nums.size() - 1;
            while (nums[j] <= nums[i]) {
                j--;
            }
            
            // Swap nums[i] and nums[j]
            swap(nums[i], nums[j]);
        }
        
        // Reverse the elements on the right side of i
        reverse(nums.begin() + i + 1, nums.end());
    }
};
```

## Test Cases
```
Input: [1, 2, 3]
Output: [1, 3, 2]
Input: [3, 2, 1]
Output: [1, 2, 3]
Input: [1, 1, 5]
Output: [1, 5, 1]
```

## Key Takeaways
- The algorithm works by finding the first decreasing element from the right and swapping it with the smallest element greater than it on the right side.
- The elements on the right side are then reversed to get the next permutation.
- If no decreasing element is found, the array is the last permutation, so the function returns the first permutation.