# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range. The problem can be solved by finding the common prefix of the binary representation of m and n, as this prefix will be present in all numbers in the range. For example, given the range [5, 7], the binary representations are 101, 110, and 111, so the bitwise AND of all numbers in this range is 100 (4 in decimal).

## Approach
The algorithm works by shifting both m and n to the right until they are equal, effectively removing the last bit where they differ. The number of shifts is then used to create a mask with the same number of leading ones as the common prefix, which is then shifted to the left to get the bitwise AND of all numbers in the range.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

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
        // create a mask with the same number of leading ones as the common prefix
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
- The bitwise AND operation has a property that it will result in 1 only if both the corresponding bits are 1.
- The common prefix of the binary representation of two numbers can be found by shifting them to the right until they are equal.
- The number of shifts required to make two numbers equal is equal to the number of bits that differ between them.