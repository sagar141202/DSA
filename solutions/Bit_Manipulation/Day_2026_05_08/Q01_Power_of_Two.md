# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x, where x is an integer. For example, 1, 2, 4, 8, 16 are all powers of two. The function should return `true` if `n` is a power of two, and `false` otherwise. The input `n` is a 32-bit signed integer, and it can be any value between -2^31 and 2^31 - 1.

## Approach
The approach is to use bit manipulation to check if the number is a power of two. A power of two has exactly one bit set to 1 in its binary representation. We can use the bitwise AND operator to check this property. If a number is a power of two, then it has no bits in common with the number one less than it.

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
        // edge case: n should be positive
        if (n <= 0) return false;
        
        // a power of two has exactly one bit set to 1 in its binary representation
        // so, doing a bitwise AND operation with the number one less than it will result in zero
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
- The bitwise AND operator can be used to check this property.
- The time complexity of the solution is constant, making it efficient for large inputs.