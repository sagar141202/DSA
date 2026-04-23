# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a subarray within the array. A subarray is a contiguous subset of the array. The product of a subarray is the product of all the integers in the subarray. The maximum product subarray problem is a variation of the maximum subarray problem, where instead of finding the maximum sum, we need to find the maximum product. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3]` with a product of 6.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is because a negative number can turn a maximum product into a minimum product and vice versa. We initialize two variables, `max_product` and `min_product`, to the first element of the array and then iterate through the rest of the array, updating these variables at each step.

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
        if (nums.empty()) return 0;
        
        int max_product = nums[0];
        int min_product = nums[0];
        int result = nums[0];
        
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < 0) {
                swap(max_product, min_product);
            }
            
            max_product = max(nums[i], max_product * nums[i]);
            min_product = min(nums[i], min_product * nums[i]);
            
            result = max(result, max_product);
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
- We need to track both the maximum and minimum product up to each position in the array.
- A negative number can turn a maximum product into a minimum product and vice versa.
- The time complexity is O(n) because we only need to iterate through the array once.