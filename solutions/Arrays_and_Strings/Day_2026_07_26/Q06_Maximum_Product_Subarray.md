# Maximum Product Subarray

## Problem Statement
Given an integer array `nums`, find the contiguous subarray within the array that has the largest product. The subarray should have at least one number. The product of an empty subarray is considered to be 0. The input array may contain both positive and negative numbers. For example, given the array `[-2,3,-4]`, the maximum product subarray is `[-2,3,-4]` with a product of `24`. Another example is the array `[1, -2, 3, 0, -2, -3, 2]`, where the maximum product subarray is `[-2, -3, 2]` or `[3, 0, -2, -3, 2]` both with a product of `12` or `0` if the subarray is empty.

## Approach
The algorithm uses dynamic programming to track the maximum and minimum product up to each position in the array. This is necessary because a negative number can become the maximum product if multiplied by another negative number. The maximum product at each position is updated based on the current number, the maximum product ending at the previous position, and the minimum product ending at the previous position.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // Handle edge case where input array is empty
        if (nums.empty()) return 0;
        
        // Initialize variables to track maximum and minimum product
        int maxSoFar = nums[0];
        int minSoFar = nums[0];
        int result = nums[0];
        
        // Iterate through the array starting from the second number
        for (int i = 1; i < nums.size(); i++) {
            // If current number is negative, swap maxSoFar and minSoFar
            if (nums[i] < 0) {
                swap(maxSoFar, minSoFar);
            }
            
            // Update maxSoFar and minSoFar
            maxSoFar = max(nums[i], maxSoFar * nums[i]);
            minSoFar = min(nums[i], minSoFar * nums[i]);
            
            // Update result
            result = max(result, maxSoFar);
        }
        
        return result;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {-2, 3, -4};
    cout << "Maximum product subarray: " << solution.maxProduct(nums) << endl;
    return 0;
}
```

## Test Cases
```
Input: [-2,3,-4]
Output: 24
Input: [1, -2, 3, 0, -2, -3, 2]
Output: 12
Input: [0, 0, 0]
Output: 0
```

## Key Takeaways
- The algorithm must track both the maximum and minimum product up to each position because a negative number can become the maximum product if multiplied by another negative number.
- The space complexity is O(1) because only a constant amount of space is used, regardless of the size of the input array.
- The time complexity is O(n) because the algorithm iterates through the input array once.