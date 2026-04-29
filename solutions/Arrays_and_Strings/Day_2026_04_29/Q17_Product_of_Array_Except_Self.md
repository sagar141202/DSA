# Product of Array Except Self

## Problem Statement
Given an array of integers, return an array where each element at index i is equal to the product of all numbers in the input array except the one at index i. The length of the input array will be at least 1 and not more than 10,000. The input array will only contain integers between -100,000 and 100,000. The output array should have the same length as the input array. For example, if the input array is [1, 2, 3, 4], the output array should be [24, 12, 8, 6] because 24 = 2 * 3 * 4, 12 = 1 * 3 * 4, 8 = 1 * 2 * 4, and 6 = 1 * 2 * 3.

## Approach
The approach to solve this problem is to calculate the prefix product and suffix product for each element in the array. The prefix product is the product of all numbers to the left of the current number, and the suffix product is the product of all numbers to the right of the current number. We can then multiply the prefix product and suffix product to get the product of all numbers except the current number.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> output(n, 1);
    
    // Calculate prefix product
    for (int i = 1; i < n; i++) {
        output[i] = output[i - 1] * nums[i - 1];
    }
    
    // Calculate suffix product and update output
    int suffixProduct = 1;
    for (int i = n - 1; i >= 0; i--) {
        output[i] *= suffixProduct;
        suffixProduct *= nums[i];
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
- We can solve this problem in O(n) time complexity by calculating the prefix and suffix product in two separate passes.
- We can avoid using extra space by updating the output array in-place.
- The problem can be solved using dynamic programming techniques, but it's not necessary in this case.