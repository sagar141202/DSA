# Power of Two

## Problem Statement
Given an integer `n`, write a function that checks if it is a power of two. A power of two is a number that can be expressed as 2^x where x is a non-negative integer. The function should return `true` if `n` is a power of two, and `false` otherwise. The input `n` is a 32-bit signed integer, and it can be in the range [-2^31, 2^31 - 1]. For example, the function should return `true` for inputs 1, 2, 4, 8, and `false` for inputs 3, 5, 6.

## Approach
The algorithm uses bit manipulation to check if a number is a power of two. A power of two has exactly one bit set to 1 in its binary representation. We can use this property to check if a number is a power of two. We can use the bitwise AND operator (&) to check if a number is a power of two.

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
        // A power of two has exactly one bit set to 1 in its binary representation
        // We can use the bitwise AND operator (&) to check if a number is a power of two
        // If n is a power of two, then n & (n - 1) will be zero
        return n > 0 && (n & (n - 1)) == 0;
    }
};
```

## Test Cases
```
Input: 1
Output: true
Input: 3
Output: false
Input: 16
Output: true
```

## Key Takeaways
- A power of two has exactly one bit set to 1 in its binary representation.
- The bitwise AND operator (&) can be used to check if a number is a power of two.
- The condition `n > 0` is necessary to handle the case where `n` is zero, because zero is not a power of two.