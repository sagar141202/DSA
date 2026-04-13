# Product of Array Except Self

## Problem Statement
Given an array of integers, return an array where each element at index `i` is the product of all numbers in the input array except the number at index `i`. The length of the input array will be at least 1 and not more than 20,000. The input array will contain only integers between -100,000 and 100,000. The output array should have the same length as the input array, and each element should be the product of all other numbers. For example, if the input array is `[1, 2, 3, 4]`, the output array should be `[24, 12, 8, 6]`.

## Approach
The approach to solve this problem is to calculate the prefix products and suffix products for each element in the array. The product of all numbers except the number at index `i` can be calculated as the product of the prefix product up to index `i-1` and the suffix product from index `i+1` to the end.

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
    
    // Calculate prefix products
    for (int i = 1; i < n; i++) {
        output[i] = output[i-1] * nums[i-1];
    }
    
    // Calculate suffix products and update output
    int suffixProduct = 1;
    for (int i = n-1; i >= 0; i--) {
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
- Use prefix and suffix products to efficiently calculate the product of all numbers except the number at each index.
- The space complexity can be optimized to O(1) by using the output array to store the prefix products and then updating it with the suffix products.