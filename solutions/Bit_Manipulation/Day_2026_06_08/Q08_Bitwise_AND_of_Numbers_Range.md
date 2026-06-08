# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range. The input values m and n are integers, and the result should also be an integer. For example, the bitwise AND of numbers in the range [5, 7] is 4, because 5 = 101 in binary, 6 = 110 in binary, and 7 = 111 in binary. The bitwise AND of these numbers is 100, which is 4 in decimal.

## Approach
The algorithm involves finding the common prefix of the binary representation of m and n. This common prefix is the bitwise AND of all numbers in the range [m, n]. We can find the common prefix by shifting both m and n to the right until they are equal.

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
        while (m != n) {
            m >>= 1;
            n >>= 1;
            shift++;
        }
        // the common prefix is the bitwise AND of all numbers in the range
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
- The bitwise AND operation has a property that a & b = a if a is a prefix of b.
- The common prefix of the binary representation of m and n can be found by shifting both m and n to the right until they are equal.
- The bitwise AND of all numbers in the range [m, n] is the common prefix of the binary representation of m and n.