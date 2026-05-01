# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x, where x is an integer. The function should return `true` if `n` is a power of two, and `false` otherwise. The input `n` is a 32-bit signed integer. For example, `n = 8` is a power of two because it can be expressed as 2^3, while `n = 10` is not.

## Approach
The algorithm uses bit manipulation to check if a number is a power of two. If a number is a power of two, its binary representation has exactly one bit set to 1. We can use this property to check if a number is a power of two. The idea is to use the bitwise AND operator to check if a number is a power of two.

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
        // If n is less than or equal to 0, it is not a power of two
        if (n <= 0) return false;
        
        // Use bitwise AND operator to check if n is a power of two
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
- A power of two has exactly one bit set to 1 in its binary representation.
- The bitwise AND operator can be used to check if a number is a power of two.
- The time complexity of the solution is O(1) because it only involves a constant number of operations.