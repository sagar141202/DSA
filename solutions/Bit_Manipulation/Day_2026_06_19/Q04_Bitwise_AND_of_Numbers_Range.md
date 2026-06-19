# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers, find the bitwise AND of all numbers in that range. The range is defined by two integers, `left` and `right`, where `left` is the smallest number in the range and `right` is the largest number in the range. The bitwise AND of two numbers is the number obtained by performing a bitwise AND operation on the binary representations of the two numbers. For example, the bitwise AND of 5 (101 in binary) and 3 (011 in binary) is 1 (001 in binary). The function should return the bitwise AND of all numbers in the range `[left, right]`. The constraints are `0 <= left <= right <= 2^31 - 1`.

## Approach
The algorithm uses the property of bitwise AND that `a & b` will have all the common prefix bits set as 1 and the rest as 0. We find the common prefix of `left` and `right` by shifting both numbers to the right until they are equal. The common prefix is then shifted back to the left to get the result.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int shift = 0;
        // find the common prefix
        while (left < right) {
            left >>= 1;
            right >>= 1;
            shift++;
        }
        // shift the common prefix back to the left
        return left << shift;
    }
};
```

## Test Cases
```
Input: left = 5, right = 7
Output: 4
Input: left = 1, right = 2
Output: 0
```

## Key Takeaways
- The bitwise AND operation can be used to find the common prefix of two numbers.
- Shifting numbers to the right can be used to find the common prefix.
- The common prefix can be shifted back to the left to get the result.