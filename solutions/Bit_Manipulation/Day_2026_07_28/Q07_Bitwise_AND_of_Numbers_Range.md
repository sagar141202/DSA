# Bitwise AND of Numbers Range

## Problem Statement
Given a range of numbers from m to n, where 0 <= m <= n, find the bitwise AND of all numbers in this range. The bitwise AND operation compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0. For example, the bitwise AND of 5 (101) and 3 (011) is 1 (001). The function should return the bitwise AND of all numbers in the range [m, n].

## Approach
The algorithm involves finding the common prefix of the binary representation of m and n, which will be the bitwise AND of all numbers in the range. This can be achieved by shifting both m and n to the right until they are equal. The number of shifts required to make m and n equal will give us the number of bits to shift back to the left to get the common prefix.

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
            // Shift both m and n to the right by 1 bit
            m >>= 1;
            n >>= 1;
            
            // Increment the shift count
            shift++;
        }
        
        // Shift m back to the left by the shift count to get the common prefix
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
- Shifting bits to the right is equivalent to dividing by 2, and shifting bits to the left is equivalent to multiplying by 2.
- The number of shifts required to make two numbers equal can be used to find the common prefix.