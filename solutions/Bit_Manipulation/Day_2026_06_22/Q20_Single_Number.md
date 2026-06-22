# Single Number

## Problem Statement
Given a non-empty array of integers, every element appears twice except for one. Find that single one. The input array will have at least one element, and all elements will be in the range [-2^31, 2^31 - 1]. The solution should have a linear time complexity and use a constant amount of space. For example, if the input is [2,2,1], the output should be 1, and if the input is [4,1,2,1,2], the output should be 4.

## Approach
The algorithm uses bitwise XOR operation to find the single number. The XOR of a number with itself is 0, and the XOR of a number with 0 is the number itself. By XORing all numbers in the array, the numbers that appear twice will cancel out, leaving the single number.

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
        // XOR all numbers in the array
        for (int num : nums) {
            result ^= num;
        }
        return result;
    }
};
```

## Test Cases
```
Input: [2,2,1]
Output: 1
Input: [4,1,2,1,2]
Output: 4
```

## Key Takeaways
- The XOR operation has a property that `a ^ a = 0` and `a ^ 0 = a`, which makes it useful for finding the single number in the array.
- The solution has a linear time complexity because it only needs to iterate through the array once.
- The solution uses a constant amount of space because it only needs to store the result of the XOR operation.