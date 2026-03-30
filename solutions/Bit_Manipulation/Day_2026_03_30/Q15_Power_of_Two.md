# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x where x is an integer. For example, 1, 2, 4, 8 are powers of two, while 3, 5, 6 are not. The function should return `true` if `n` is a power of two and `false` otherwise. The input `n` is a 32-bit signed integer.

## Approach
We can use bit manipulation to solve this problem. The idea is to check if the binary representation of `n` has exactly one '1' bit. We can use the bitwise AND operator to achieve this. If `n` is a power of two, then its binary representation has exactly one '1' bit, and subtracting 1 from it will give us a number that has all the bits to the right of the '1' bit set to '1' and all other bits set to '0'.

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
        // check if n is less than or equal to 0
        if (n <= 0) return false;
        
        // use bitwise AND operator to check if n is a power of two
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
- A power of two has exactly one '1' bit in its binary representation.
- The bitwise AND operator can be used to check if a number is a power of two.
- The function should return `false` for input `n` less than or equal to 0.