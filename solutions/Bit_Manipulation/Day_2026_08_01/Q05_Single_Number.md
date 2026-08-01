# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single number. The solution should have a linear time complexity and use constant space. For example, given the array `nums = [2, 2, 1]`, the function should return `1`, because `1` appears only once in the array. Another example, given the array `nums = [4, 1, 2, 1, 2]`, the function should return `4`, because `4` appears only once in the array.

## Approach
The algorithm uses bit manipulation to find the single number. It iterates over the array and performs a bitwise XOR operation between each number and the result. The XOR operation has the property that `a ^ a = 0` and `a ^ 0 = a`, so all numbers that appear twice will cancel out, leaving only the single number.

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
        // Iterate over the array and perform a bitwise XOR operation
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
};
```

## Test Cases
```
Input: nums = [2, 2, 1]
Output: 1
Input: nums = [4, 1, 2, 1, 2]
Output: 4
```

## Key Takeaways
- The XOR operation can be used to find the single number in an array where every element appears twice except for one.
- The solution has a linear time complexity and uses constant space, making it efficient for large inputs.
- The algorithm is simple and easy to implement, but it requires a good understanding of bit manipulation and the properties of the XOR operation.