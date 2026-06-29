# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x, where x is an integer. The function should return `true` if `n` is a power of two, and `false` otherwise. The input `n` is a 32-bit signed integer. For example, if `n = 8`, the function should return `true` because 8 can be expressed as 2^3. If `n = 10`, the function should return `false` because 10 cannot be expressed as a power of two.

## Approach
The approach is to use bit manipulation to check if the number is a power of two. A power of two in binary representation has exactly one bit set to 1 (the bit in the place that corresponds to that power of two). We can use this property to determine if a number is a power of two.

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
        
        // Use bit manipulation to check if the number is a power of two
        // A power of two in binary representation has exactly one bit set to 1
        return (n & (n - 1)) == 0;
    }
};
```

## Test Cases
```
Input: n = 8
Output: true
Input: n = 10
Output: false
```

## Key Takeaways
- A power of two in binary representation has exactly one bit set to 1.
- The expression `n & (n - 1)` can be used to check if a number is a power of two.
- The time complexity of this solution is O(1), making it efficient for large inputs.