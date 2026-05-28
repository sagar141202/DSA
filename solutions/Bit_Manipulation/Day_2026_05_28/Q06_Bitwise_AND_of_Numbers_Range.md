# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range. The input values m and n are integers, and the result should be an integer as well. For example, given the range [5, 7], the bitwise AND of 5, 6, and 7 is 4, because 5 = 101 in binary, 6 = 110 in binary, and 7 = 111 in binary. The bitwise AND of these numbers is 100 in binary, which is 4 in decimal.

## Approach
The algorithm involves finding the common prefix of the binary representations of m and n. This common prefix will be the bitwise AND of all numbers in the range [m, n]. We can achieve this by shifting both m and n to the right until they are equal, keeping track of the number of shifts. The bitwise AND of the range will be the common prefix shifted back to its original position.

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
        // Initialize the shift count to 0
        int shift = 0;
        
        // Continue shifting until m and n are equal
        while (m != n) {
            // Shift m and n to the right by 1 bit
            m >>= 1;
            n >>= 1;
            // Increment the shift count
            shift++;
        }
        
        // Return the result by shifting m back to its original position
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
- The bitwise AND operation has a property that `a & b` will result in a value that has all the common prefix bits of `a` and `b` set to 1, and all other bits set to 0.
- By shifting both numbers to the right until they are equal, we effectively find the common prefix of their binary representations.
- The number of shifts required to make `m` and `n` equal represents the number of bits that are not part of the common prefix.