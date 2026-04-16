# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. The function should return `true` if `n` is a power of two, and `false` otherwise. The input `n` is a 32-bit signed integer, and it can be any integer between `-2^31` and `2^31 - 1`. For example, if `n = 8`, the function should return `true` because `8` is `2^3`. If `n = 10`, the function should return `false` because `10` is not a power of two.

## Approach
The approach is to use bit manipulation to check if the given number is a power of two. A number is a power of two if it has exactly one bit set in its binary representation. We can use the bitwise AND operator to check this.

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
        if (n <= 0) return false;
        
        // A number is a power of two if it has exactly one bit set in its binary representation
        // We can use the bitwise AND operator to check this
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

Input: 1
Output: true

Input: 0
Output: false
```

## Key Takeaways
- A number is a power of two if it has exactly one bit set in its binary representation.
- The bitwise AND operator can be used to check if a number is a power of two.
- The time complexity of the solution is O(1) because it involves a constant number of operations.