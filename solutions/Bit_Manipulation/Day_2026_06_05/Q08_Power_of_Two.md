# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x, where x is an integer. The function should return `true` if `n` is a power of two and `false` otherwise. The input `n` is a 32-bit signed integer, and the function should handle cases where `n` is less than or equal to 0.

## Approach
The approach is to use bit manipulation to check if the binary representation of `n` has exactly one bit set to 1. This is because powers of two have a unique property where their binary representation has only one 1 bit. We can use the bitwise AND operator to achieve this.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isPowerOfTwo(int n) {
        // If n is less than or equal to 0, it is not a power of two
        if (n <= 0) {
            return false;
        }
        // Use bitwise AND to check if n has exactly one 1 bit
        return (n & (n - 1)) == 0;
    }
};
```

## Test Cases
```
Input: 8
Output: true
Input: 10
Output: false
Input: 16
Output: true
Input: 0
Output: false
```

## Key Takeaways
- A power of two has exactly one 1 bit in its binary representation.
- The bitwise AND operator (`&`) can be used to check if a number has exactly one 1 bit.
- The expression `n & (n - 1)` is a common idiom to check if a number is a power of two.