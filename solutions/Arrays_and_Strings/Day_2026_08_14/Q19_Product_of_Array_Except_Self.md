# Product of Array Except Self

## Problem Statement
Given an array `nums` of `n` integers where `n > 1`, return an array `output` such that `output[i]` is equal to the product of all the numbers in `nums` except `nums[i]`. The constraint is that the solution should not use division and should have a time complexity of O(n). For example, if `nums = [1, 2, 3, 4]`, then `output = [24, 12, 8, 6]`.

## Approach
The algorithm involves calculating the prefix and postfix products for each element in the array, then multiplying these two products together to get the product of all numbers except the current one. This approach ensures that we do not use division and achieve the required time complexity.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int length = nums.size();
        std::vector<int> answer(length);
        
        // answer[i] contains the product of all the numbers to the left.
        answer[0] = 1;
        for (int i = 1; i < length; i++) {
            answer[i] = nums[i - 1] * answer[i - 1];
        }
        
        // R contains the product of all the numbers to the right
        int R = 1;
        for (int i = length - 1; i >= 0; i--) {
            answer[i] = answer[i] * R;
            R *= nums[i];
        }
        
        return answer;
    }
};
```

## Test Cases
```
Input: [1, 2, 3, 4]
Output: [24, 12, 8, 6]
Input: [1]
Output: Not applicable as n > 1
```

## Key Takeaways
- We can solve this problem without using division by calculating prefix and postfix products.
- The space complexity can be reduced to O(1) if we are allowed to modify the input array, but in this solution, we use O(n) space for the output array.
- This problem demonstrates how to apply the concept of prefix and postfix calculations to solve array-related problems efficiently.