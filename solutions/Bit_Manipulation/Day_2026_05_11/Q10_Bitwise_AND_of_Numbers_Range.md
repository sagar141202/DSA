# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, find the bitwise AND of all numbers in this range. The bitwise AND operation compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0. For example, given the range [5, 7], the bitwise AND of all numbers in this range is 4, because 5 = 101, 6 = 110, and 7 = 111 in binary, and the bitwise AND of these numbers is 100, which is 4 in decimal.

## Approach
The approach is to find the common prefix of the binary representation of m and n, and then append zeros to the end of the prefix. This is because the bitwise AND operation will set all bits to the right of the common prefix to 0. We can find the common prefix by shifting both m and n to the right until they are equal.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        // shift both m and n to the right until they are equal
        int shift = 0;
        while (m != n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // append zeros to the end of the common prefix
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
- The bitwise AND operation can be used to find the common prefix of the binary representation of two numbers.
- Shifting both numbers to the right until they are equal will give us the common prefix.
- Appending zeros to the end of the common prefix will give us the bitwise AND of all numbers in the range.