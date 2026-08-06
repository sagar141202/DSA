# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, find the bitwise AND of all numbers in this range. The bitwise AND operation compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0. For example, the bitwise AND of 5 (101) and 3 (011) is 1 (001).

## Approach
The algorithm uses bit manipulation to find the common prefix of the binary representation of m and n, which is the bitwise AND of all numbers in the range. This is because the bitwise AND operation will preserve the common prefix of the binary representation of two numbers.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        // find the common prefix of m and n
        int shift = 0;
        while (m < n) {
            // right shift both m and n by 1
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // restore the common prefix to its original position
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
- Right shifting a number by 1 bit is equivalent to dividing it by 2.
- Left shifting a number by 1 bit is equivalent to multiplying it by 2.