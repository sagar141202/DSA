# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^n where n is an integer. The function should return `true` if the number is a power of two and `false` otherwise. The input `n` is a 32-bit signed integer. For example, the function should return `true` for inputs `1`, `2`, `4`, `8`, etc., and `false` for inputs `3`, `5`, `6`, `7`, etc. The constraints are `-(2^31) <= n <= 2^31 - 1`.

## Approach
The approach to solve this problem is to use bit manipulation. We can use the property that in binary representation, powers of two have exactly one bit set to 1. We can use bitwise operations to check this property. The algorithm involves checking if the number is positive and if it has exactly one bit set to 1.

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
        // Check if the number is positive
        if (n <= 0) {
            return false;
        }
        // Check if the number has exactly one bit set to 1
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
- The bitwise AND operation `&` can be used to check if a number has exactly one bit set to 1.
- The expression `n & (n - 1)` can be used to check if a number is a power of two.