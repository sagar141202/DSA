# Power of Two

## Problem Statement
Given an integer `n`, return `true` if it is a power of two, otherwise return `false`. A power of two is a number that can be expressed as 2 raised to an integer power, i.e., `n = 2^x` where `x` is an integer. The input `n` is within the range `[0, 2^31 - 1]`. For example, `1`, `2`, `4`, `8` are all powers of two, while `3`, `5`, `6` are not.

## Approach
The approach is to use bit manipulation to check if the number is a power of two. A power of two has exactly one bit set to 1 in its binary representation. We can use the bitwise AND operator to check this property. If `n` is a power of two, then `n & (n - 1)` will be zero.

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
        // if n is less than or equal to 0, it is not a power of two
        if (n <= 0) return false;
        // if n is a power of two, then n & (n - 1) will be zero
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
- A power of two has exactly one bit set to 1 in its binary representation.
- The bitwise AND operator `&` can be used to check if a number is a power of two.
- The expression `n & (n - 1)` will be zero if `n` is a power of two.