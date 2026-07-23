# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, find the bitwise AND of all numbers in this range. The bitwise AND operation compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0. For example, the bitwise AND of 5 (101) and 3 (011) is 1 (001).

## Approach
The algorithm involves finding the common prefix of the binary representation of m and n, then appending zeros to get the result. This is because the bitwise AND operation will result in zeros for all bits where m and n have different values. The common prefix will be the result of the bitwise AND operation.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        // find the number of common prefix bits
        int shift = 0;
        while (m < n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // append zeros to the common prefix
        return m << shift;
    }
};
```

## Test Cases
```
Input: m = 5, n = 7
Output: 4
Input: m = 0, n = 0
Output: 0
```

## Key Takeaways
- The bitwise AND operation can be used to find the common prefix of two binary numbers.
- Right shifting both numbers by the same amount does not change the result of the bitwise AND operation.
- The result of the bitwise AND operation can be obtained by appending zeros to the common prefix of the binary representation of the input numbers.