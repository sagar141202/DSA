# Power of Two

## Problem Statement
Given an integer n, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x, where x is an integer. For example, 1, 2, 4, 8 are powers of two, while 3, 5, 6, 7 are not. The function should return true if the number is a power of two and false otherwise. The input integer n will be in the range [0, 2^31 - 1].

## Approach
The approach is to use bitwise operations to check if the number is a power of two. A number is a power of two if it has exactly one '1' bit in its binary representation. We can use the bitwise AND operator (&) to check this.

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
        // If n is less than or equal to 0, it cannot be a power of two
        if (n <= 0) {
            return false;
        }
        // A number is a power of two if it has exactly one '1' bit in its binary representation
        // We can use the bitwise AND operator (&) to check this
        return (n & (n - 1)) == 0;
    }
};
```

## Test Cases
```
Input: 1
Output: true
Input: 16
Output: true
Input: 218
Output: false
```

## Key Takeaways
- A number is a power of two if it has exactly one '1' bit in its binary representation.
- The bitwise AND operator (&) can be used to check if a number is a power of two.
- The expression `n & (n - 1)` will be zero if and only if `n` is a power of two.