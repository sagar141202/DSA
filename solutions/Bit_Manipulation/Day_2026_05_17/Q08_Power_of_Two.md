# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x, where x is an integer. For example, 1, 2, 4, 8 are all powers of two, while 3, 5, 6 are not. The function should return `true` if `n` is a power of two and `false` otherwise. The input `n` will be in the range [0, 2^31 - 1].

## Approach
The approach is to use bit manipulation to check if the binary representation of `n` has exactly one bit set to 1. If `n` is a power of two, its binary representation will have only one 1 bit. We can use the bitwise AND operator to check this.

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
        // if n is less than or equal to 0, it's not a power of two
        if (n <= 0) return false;
        // use bitwise AND operator to check if n has exactly one 1 bit
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
```

## Key Takeaways
- A power of two has exactly one 1 bit in its binary representation.
- The bitwise AND operator can be used to check if a number has exactly one 1 bit.
- The expression `n & (n - 1)` will be zero if and only if `n` is a power of two.