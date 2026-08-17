# Maximum Subarray (Kadane's Algorithm)

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. The array may contain both positive and negative integers. For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`, the maximum subarray sum is `6` which is the sum of the subarray `[4,-1,2,1]`. If the array is empty, return `0`.

## Approach
Kadane's algorithm is used to find the maximum sum of a subarray within an array. It works by scanning the entire array and at each position, it decides whether to continue the current subarray or start a new one. The algorithm keeps track of the maximum sum of subarray ending at each position.

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
        // Initialize the maximum sum and the current sum
        int max_sum = nums[0];
        int current_sum = nums[0];
        
        // Iterate over the array starting from the second element
        for (int i = 1; i < nums.size(); i++) {
            // Update the current sum by choosing the maximum between the current number and the sum of the current number and the previous current sum
            current_sum = max(nums[i], current_sum + nums[i]);
            // Update the maximum sum if the current sum is greater
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
Input: nums = [0]
Output: 0
Input: nums = [-1]
Output: -1
```

## Key Takeaways
- Kadane's algorithm is an efficient solution for finding the maximum sum of a subarray within an array.
- The algorithm works by keeping track of the maximum sum of subarray ending at each position and updating it accordingly.
- The time complexity of Kadane's algorithm is O(n), where n is the number of elements in the array.