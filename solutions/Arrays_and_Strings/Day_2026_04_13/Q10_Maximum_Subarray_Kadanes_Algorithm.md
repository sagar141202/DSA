# Maximum Subarray (Kadane's Algorithm)

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. The array can contain both positive and negative integers. For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`, the maximum subarray sum is `6` which is the sum of the subarray `[4,-1,2,1]`.

## Approach
Kadane's algorithm is used to find the maximum sum of a subarray within an array. It iterates through the array, at each step deciding whether to continue the current subarray or start a new one. The algorithm keeps track of the maximum sum found so far.

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
        // Initialize the maximum sum and the current sum to the first element of the array
        int max_sum = nums[0];
        int current_sum = nums[0];
        
        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.size(); i++) {
            // Update the current sum to be the maximum of the current number and the sum of the current number and the previous current sum
            current_sum = max(nums[i], current_sum + nums[i]);
            // Update the maximum sum to be the maximum of the current maximum sum and the current sum
            max_sum = max(max_sum, current_sum);
        }
        
        // Return the maximum sum
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
- Kadane's algorithm is an efficient solution for finding the maximum sum of a subarray within an array.
- The algorithm has a time complexity of O(n) and a space complexity of O(1), making it suitable for large inputs.
- The algorithm iterates through the array only once, making it efficient for real-time applications.