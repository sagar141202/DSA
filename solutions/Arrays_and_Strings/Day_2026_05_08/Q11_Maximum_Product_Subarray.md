# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the contiguous subarray within the array that has the largest product. The product of an empty subarray is considered to be 0. It is guaranteed that the product of any subarray does not exceed 2^31 - 1. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3,-4]` which has a product of `24`. Another example is the array `[1, -2, -3, 0, 7, -8, -2]`, where the maximum product subarray is `[-2, -3, 0, 7, -8, -2]` but since we need a contiguous subarray, the maximum product will be of subarray `[-2, -3, 0]` or `[7, -8, -2]` but the maximum product will be of subarray `7` or `[-2, -3]` which is `[-2, -3]` or `7`. The maximum product subarray is `[-2, -3]` or `[7]`.

## Approach
We will use dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can turn a maximum product into a minimum product. We will maintain two arrays, `maxDP` and `minDP`, where `maxDP[i]` and `minDP[i]` represent the maximum and minimum product up to index `i` respectively.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <climits>

int maxProduct(std::vector<int>& nums) {
    int n = nums.size();
    std::vector<int> maxDP(n, 0);
    std::vector<int> minDP(n, 0);
    maxDP[0] = minDP[0] = nums[0];
    int result = nums[0];

    for (int i = 1; i < n; i++) {
        if (nums[i] < 0) {
            int temp = maxDP[i-1];
            maxDP[i-1] = minDP[i-1];
            minDP[i-1] = temp;
        }
        maxDP[i] = std::max(nums[i], maxDP[i-1] * nums[i]);
        minDP[i] = std::min(nums[i], minDP[i-1] * nums[i]);
        result = std::max(result, maxDP[i]);
    }
    return result;
}

int main() {
    std::vector<int> nums = {-2, 3, -4};
    std::cout << maxProduct(nums) << std::endl;
    return 0;
}
```

## Test Cases
```
Input: [-2, 3, -4]
Output: 24
Input: [1, -2, -3, 0, 7, -8, -2]
Output: 112
```

## Key Takeaways
- We use dynamic programming to track the maximum and minimum product up to each position in the array.
- We maintain two arrays, `maxDP` and `minDP`, where `maxDP[i]` and `minDP[i]` represent the maximum and minimum product up to index `i` respectively.
- We update `maxDP` and `minDP` based on whether the current number is positive or negative.