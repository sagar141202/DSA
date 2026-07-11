# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as $2^x$ where $x$ is an integer. The function should return `true` if `n` is a power of two, and `false` otherwise. The input `n` is a 32-bit signed integer, so $-2^{31} \leq n \leq 2^{31} - 1$. For example, the function should return `true` for inputs `1`, `2`, `4`, `8`, ... and `false` for inputs `3`, `5`, `6`, `7`, ... .

## Approach
The approach is to use bit manipulation to check if the number is a power of two. A power of two has exactly one bit set to 1 in its binary representation. We can use the bitwise AND operator to check this property.

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
        // edge case: n <= 0 is not a power of two
        if (n <= 0) return false;
        
        // a power of two has exactly one bit set to 1 in its binary representation
        // so, doing a bitwise AND operation with n-1 will result in 0
        return (n & (n-1)) == 0;
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
- The bitwise AND operator can be used to check if a number is a power of two.
- The time complexity of this solution is O(1) because it involves a constant number of operations.