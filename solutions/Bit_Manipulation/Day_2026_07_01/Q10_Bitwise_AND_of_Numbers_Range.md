# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, find the bitwise AND of all numbers in this range. The bitwise AND operation compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0. For example, the bitwise AND of 5 (101) and 3 (011) is 1 (001).

## Approach
The algorithm is based on finding the common prefix of the binary representation of m and n, as the bitwise AND of all numbers in the range will have the same prefix. We shift both m and n to the right until they are equal, and the number of shifts will determine the number of common prefix bits.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        // shift m and n to the right until they are equal
        int shift = 0;
        while (m < n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // the common prefix is m, and we need to shift it back to its original position
        return m << shift;
    }
};
```

## Test Cases
```
Input: m = 5, n = 7
Output: 4
Input: m = 1, n = 2
Output: 0
```

## Key Takeaways
- The bitwise AND operation can be used to find the common prefix of two binary numbers.
- Shifting numbers to the right can be used to remove the least significant bits.
- The number of shifts can be used to determine the number of common prefix bits.