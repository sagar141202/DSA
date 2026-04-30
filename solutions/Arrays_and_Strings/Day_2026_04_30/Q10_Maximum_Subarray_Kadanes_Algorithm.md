# Maximum Subarray (Kadane's Algorithm)

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. The array may contain both positive and negative integers. For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`, the maximum subarray sum is `6` which is the sum of the subarray `[4,-1,2,1]`.

## Approach
Kadane's algorithm is used to find the maximum sum of a subarray within an array. It works by scanning the entire array and at each position finding the maximum sum of the subarray ending at that position. The algorithm keeps track of the maximum sum found so far.

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
        // Initialize maximum sum and current sum to the first element of the array
        int max_sum = nums[0];
        int current_sum = nums[0];

        // Iterate over the array starting from the second element
        for (int i = 1; i < nums.size(); i++) {
            // Update current sum to be the maximum of the current number and the sum of the current number and the previous current sum
            current_sum = max(nums[i], current_sum + nums[i]);
            // Update maximum sum to be the maximum of the current maximum sum and the current sum
            max_sum = max(max_sum, current_sum);
        }

        // Return the maximum sum found
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
- The algorithm works by keeping track of the maximum sum found so far and the current sum of the subarray ending at the current position.
- The time complexity of Kadane's algorithm is O(n), where n is the number of elements in the array.