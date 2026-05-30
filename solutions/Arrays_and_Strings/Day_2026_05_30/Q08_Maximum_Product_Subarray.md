# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the maximum product of a subarray within the array. A subarray is a contiguous subset of the array. The input array will have a length of at least 1 and at most 20000 elements, with each element ranging from -10^5 to 10^5. The maximum product subarray can be obtained by considering all possible subarrays and calculating their product. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[3,-4]` with a product of 12, but if the array is `[-4,-3,-2]`, the maximum product subarray is `[-4]` with a product of -4.

## Approach
We use dynamic programming to track the maximum and minimum product up to each position. This is because a negative number can turn a maximum product into a minimum product and vice versa. We initialize two variables, `max_product` and `min_product`, to the first element of the array and then iterate through the rest of the array, updating these variables at each step.

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
- We need to track both the maximum and minimum product up to each position because a negative number can change the maximum product to a minimum product and vice versa.
- We initialize `max_product` and `min_product` to the first element of the array and then update them as we iterate through the rest of the array.
- We return the maximum product found so far, which is stored in the `result` variable.