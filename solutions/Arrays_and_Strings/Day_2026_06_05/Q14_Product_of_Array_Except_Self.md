# Product of Array Except Self

## Problem Statement
Given an array of integers, return an array where each element at index `i` is the product of all numbers in the input array except the one at `i`. The constraint is that the solution should be achieved in O(n) time complexity and without using division. For example, if the input array is `[1, 2, 3, 4]`, the output should be `[24, 12, 8, 6]` because `24 = 2 * 3 * 4`, `12 = 1 * 3 * 4`, `8 = 1 * 2 * 4`, and `6 = 1 * 2 * 3`.

## Approach
The algorithm involves calculating the prefix products and suffix products separately and then multiplying them to get the final result. This approach ensures that we do not use division and achieve the desired time complexity. We iterate through the array twice: once for prefix products and once for suffix products.

## Complexity
- Time: O(n)
- Space: O(1) excluding the output array, O(n) including it

## C++ Solution
```cpp
#include <vector>
using namespace std;

vector<int> productExceptSelf(vector<int>& nums) {
    int n = nums.size();
    vector<int> output(n, 1); // Initialize output array with 1s
    
    // Calculate prefix products
    int prefixProduct = 1;
    for (int i = 0; i < n; i++) {
        output[i] *= prefixProduct;
        prefixProduct *= nums[i];
    }
    
    // Calculate suffix products
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
- We can solve this problem without division by using the concept of prefix and suffix products.
- The space complexity can be optimized to O(1) if we exclude the output array from the space calculation.
- This problem is a good example of how to apply the concept of prefix and suffix arrays to solve problems involving arrays.