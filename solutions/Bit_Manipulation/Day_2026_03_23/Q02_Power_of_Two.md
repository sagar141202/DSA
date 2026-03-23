# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x where x is an integer. For example, 1, 2, 4, 8 are powers of two, while 3, 5, 6, 7 are not. The function should return `true` if `n` is a power of two and `false` otherwise. The constraint is that `n` is a 32-bit signed integer.

## Approach
We can use bit manipulation to solve this problem by checking if the binary representation of `n` has exactly one bit set to 1. If `n` is a power of two, its binary representation will have only one 1 bit. We can use the bitwise AND operator to achieve this.

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
        
        // if n has only one 1 bit in its binary representation, it is a power of two
        return (n & (n - 1)) == 0;
    }
};
```

## Test Cases
```
Input: n = 1
Output: true
Input: n = 16
Output: true
Input: n = 218
Output: false
```

## Key Takeaways
- A number is a power of two if and only if it has exactly one 1 bit in its binary representation.
- The expression `n & (n - 1)` can be used to check if a number is a power of two by verifying if it has only one 1 bit.
- This solution works because subtracting 1 from a power of two will result in a number that has all bits set to the right of the leftmost 1 bit in the original number.