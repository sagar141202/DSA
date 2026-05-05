# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range. The intuitive idea is to find the common prefix of the binary representation of m and n. For example, given a range [5, 7], the binary representation of 5 is 101 and 7 is 111. The common prefix is 1, so the bitwise AND of all numbers in this range is 1 * (2^2) = 4, and then fill the rest of the bits with 0s to get the result 4, but in this case, we can also find the result by shifting both m and n to the right until they are equal, the number of shifts is the number of common prefix bits that are not considered, then shift 1 to the left by the number of common prefix bits and subtract 1 to get the result of the bitwise AND operation.

## Approach
The algorithm is based on shifting both m and n to the right until they are equal, which effectively removes the last bit where they differ. The number of shifts is the number of bits that are not part of the common prefix. Then, shifting 1 to the left by the total number of bits minus the number of common prefix bits gives the result of the bitwise AND operation.

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
        // Initialize the shift count
        int shift = 0;
        
        // Continue shifting until m and n are equal
        while (m != n) {
            // Shift both m and n to the right
            m >>= 1;
            n >>= 1;
            
            // Increment the shift count
            shift++;
        }
        
        // Return the result by shifting 1 to the left and subtracting 1
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
- The bitwise AND operation can be performed on a range of numbers by finding the common prefix of their binary representations.
- Shifting both numbers to the right until they are equal effectively removes the last bit where they differ.
- The number of shifts is the number of bits that are not part of the common prefix, which can be used to calculate the result of the bitwise AND operation.