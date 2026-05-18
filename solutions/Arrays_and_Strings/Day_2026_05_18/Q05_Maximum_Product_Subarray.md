# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a subarray within the array. A subarray is a contiguous subset of the array. The product of a subarray is the product of all the integers in the subarray. The array may contain both positive and negative integers, and the maximum product can be obtained from a subarray that contains both positive and negative integers. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3]` with a product of `6`. However, if the array is `[-4,-3,-2]`, the maximum product subarray is `[-4,-3]` or `[-3,-2]` with a product of `12`. The constraints are that the input array `nums` will have a length between `1` and `50000`, and each integer in the array will be between `-10^5` and `10^5`.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is because a negative number can turn a maximum product into a minimum product, and vice versa. The maximum product of a subarray ending at the current position is the maximum of the current number, the product of the current number and the maximum product of the subarray ending at the previous position, and the product of the current number and the minimum product of the subarray ending at the previous position.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // Initialize the maximum and minimum product up to the current position
        int max_so_far = nums[0];
        int min_so_far = nums[0];
        int result = nums[0];
        
        // Iterate through the array starting from the second element
        for (int i = 1; i < nums.size(); i++) {
            // If the current number is negative, swap max_so_far and min_so_far
            if (nums[i] < 0) {
                swap(max_so_far, min_so_far);
            }
            
            // Update max_so_far and min_so_far
            max_so_far = max(nums[i], max_so_far * nums[i]);
            min_so_far = min(nums[i], min_so_far * nums[i]);
            
            // Update the result
            result = max(result, max_so_far);
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: nums = [2,3,-2,4]
Output: 6
Input: nums = [-2,0,-1]
Output: 0
```

## Key Takeaways
- The algorithm has a time complexity of O(n) where n is the length of the input array.
- The algorithm has a space complexity of O(1) as it only uses a constant amount of space to store the maximum and minimum product up to the current position.
- The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array.