# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, find the bitwise AND of all numbers in this range. For example, if the input is [5, 7], the output should be 5 (101 & 110 & 111 = 101 in binary, which is 5 in decimal).

## Approach
The approach involves finding the common prefix of the binary representation of m and n, then shifting the prefix to the left by the number of bits that are not part of the prefix, and finally filling the remaining bits with zeros.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int shift = 0;
        // find the common prefix of m and n
        while (m < n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // shift the prefix to the left by the number of bits that are not part of the prefix
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
Input: m = 1, n = 2
Output: 0
```

## Key Takeaways
- The bitwise AND operation can be used to find the common prefix of two binary numbers.
- Shifting a binary number to the right by one bit is equivalent to dividing it by 2.
- The number of bits that are not part of the common prefix can be found by counting the number of shifts required to make m equal to n.