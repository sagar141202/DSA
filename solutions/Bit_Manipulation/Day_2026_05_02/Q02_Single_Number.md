# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single number. The solution should have a linear time complexity and use minimal extra space. For example, given the array `[2, 2, 1]`, the function should return `1` because `1` appears only once in the array. Similarly, given the array `[4, 1, 2, 1, 2]`, the function should return `4` because `4` appears only once in the array.

## Approach
The approach is to use bitwise operations, specifically XOR, to find the single number. The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`, which can be utilized to eliminate the numbers that appear twice.

## Complexity
- Time: O(n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        // Iterate over each number in the array
        for (int num : nums) {
            // XOR the current number with the result
            result ^= num;
        }
        // The result will be the single number
        return result;
    }
};
```

## Test Cases
```
Input: [2, 2, 1]
Output: 1
Input: [4, 1, 2, 1, 2]
Output: 4
```

## Key Takeaways
- The XOR operation can be used to find the single number in an array where every element appears twice except for one.
- The solution has a linear time complexity and uses minimal extra space, making it efficient for large inputs.
- The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`, which is utilized to eliminate the numbers that appear twice.