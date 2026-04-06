# Product of Array Except Self

## Problem Statement
Given an array of integers, return an array where each element at index `i` is equal to the product of all the numbers in the input array except the one at `i`. The solution should not use division and should have a time complexity of O(n), where n is the number of elements in the input array. The input array will contain at least one element and at most 1000 elements, with each element in the range [-1000, 1000]. For example, if the input array is `[1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]`.

## Approach
The solution involves using two arrays to store the prefix and postfix products of the input array, then multiplying corresponding elements from these arrays to obtain the desired output. This approach avoids division and ensures a linear time complexity.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> output(n, 1);
    
    // Calculate prefix products
    for (int i = 1; i < n; i++) {
        output[i] = output[i - 1] * nums[i - 1];
    }
    
    // Calculate postfix products and update output
    int postfix = 1;
    for (int i = n - 1; i >= 0; i--) {
        output[i] *= postfix;
        postfix *= nums[i];
    }
    
    return output;
}
```

## Test Cases
```
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Input: [5, 10, 15, 20]
Output: [3000, 1500, 1000, 750]
```

## Key Takeaways
- To solve this problem without using division, calculate prefix and postfix products separately.
- Utilize dynamic programming principles by storing intermediate results (prefix products) to avoid redundant calculations.
- Optimize space complexity by updating the output array in-place during the postfix product calculation.