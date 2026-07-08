# Maximum Subarray (Kadane's Algorithm)

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. The array may contain both positive and negative integers. For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`, the contiguous subarray with the largest sum is `[4,-1,2,1]` with sum `6`. If the input array is empty, return `0`.

## Approach
Kadane's Algorithm is used to solve this problem. It iterates through the array, at each step deciding whether to continue the current subarray or start a new one. The algorithm keeps track of the maximum sum of subarray ending at each position.

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
        if (nums.empty()) return 0;
        
        int max_sum = nums[0];
        int current_sum = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            // Decide whether to continue the current subarray or start a new one
            current_sum = max(nums[i], current_sum + nums[i]);
            // Update the maximum sum
            max_sum = max(max_sum, current_sum);
        }
        
        return max_sum;
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
- Kadane's Algorithm is an efficient solution for finding the maximum sum of a subarray within an array.
- It has a linear time complexity, making it suitable for large inputs.
- The algorithm can be easily modified to find the maximum sum of a subarray within a 2D array or other similar problems.