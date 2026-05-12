# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x, where x is an integer. The function should return `true` if `n` is a power of two and `false` otherwise. The input `n` is a 32-bit signed integer, and the function should handle cases where `n` is less than or equal to 0. For example, the function should return `true` for inputs 1, 2, 4, 8, and `false` for inputs 3, 5, 6.

## Approach
The algorithm uses bit manipulation to check if a number is a power of two. It works by counting the number of set bits in the binary representation of the number. If a number is a power of two, it will have exactly one set bit in its binary representation.

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
        // Use bit manipulation to count the number of set bits
        return (n & (n - 1)) == 0;
    }
};
```

## Test Cases
```
Input: 1
Output: true
Input: 3
Output: false
Input: 8
Output: true
Input: 16
Output: true
Input: 20
Output: false
```

## Key Takeaways
- A number is a power of two if and only if it has exactly one set bit in its binary representation.
- The expression `n & (n - 1)` can be used to check if a number is a power of two, as it will be zero if and only if `n` is a power of two.
- Bit manipulation can be used to solve problems efficiently, especially those involving binary numbers.