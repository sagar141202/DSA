# Maximum Subarray (Kadane's Algorithm)

## Problem Statement
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. The array may contain both positive and negative numbers. For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`, the maximum subarray sum is `6` which is the sum of the subarray `[4,-1,2,1]`. If the input array is empty, return 0.

## Approach
Kadane's algorithm is used to find the maximum sum of a subarray within an array. It works by iterating over the array and at each step, it decides whether to continue the current subarray or start a new one. The maximum sum of a subarray is updated whenever a larger sum is found.

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
        
        // Iterate over the array starting from the second element
        for (int i = 1; i < nums.size(); i++) {
            // Update the current sum by choosing the maximum between the current number and the sum of the current number and the previous current sum
            current_sum = max(nums[i], current_sum + nums[i]);
            // Update the maximum sum if the current sum is larger
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
Input: nums = [0]
Output: 0
Input: nums = []
Output: 0
```

## Key Takeaways
- Kadane's algorithm is an efficient solution to find the maximum sum of a subarray within an array.
- The algorithm works by maintaining a running sum of the current subarray and updating the maximum sum whenever a larger sum is found.
- The time complexity of the algorithm is O(n), where n is the number of elements in the array, making it suitable for large inputs.