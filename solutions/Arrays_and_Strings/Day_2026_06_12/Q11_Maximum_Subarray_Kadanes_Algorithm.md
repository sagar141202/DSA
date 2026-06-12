# Maximum Subarray (Kadane's Algorithm)

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. The array can contain both positive and negative integers. For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`, the maximum subarray sum is `6` which can be obtained from the subarray `[4,-1,2,1]`.

## Approach
Kadane's algorithm is used to solve this problem, which iterates through the array and at each step, it decides whether to include the current element in the maximum subarray or start a new subarray. The algorithm keeps track of the maximum sum of subarray ending at the current position and the maximum sum of subarray seen so far.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // Initialize the maximum sum of subarray ending at the current position and the maximum sum of subarray seen so far
        int max_so_far = nums[0];
        int max_ending_here = nums[0];
        
        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.size(); i++) {
            // Update the maximum sum of subarray ending at the current position
            max_ending_here = max(nums[i], max_ending_here + nums[i]);
            
            // Update the maximum sum of subarray seen so far
            max_so_far = max(max_so_far, max_ending_here);
        }
        
        // Return the maximum sum of subarray seen so far
        return max_so_far;
    }
};
```

## Test Cases
```
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Input: nums = [1]
Output: 1
Input: nums = [5,4,-1,7,8]
Output: 23
```

## Key Takeaways
- Kadane's algorithm is an efficient solution for finding the maximum subarray sum in an array.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it suitable for large inputs.
- The algorithm can be used to find the maximum subarray sum in arrays containing both positive and negative integers.