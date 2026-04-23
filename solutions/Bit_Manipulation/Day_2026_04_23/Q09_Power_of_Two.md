# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x where x is an integer. The function should return `true` if `n` is a power of two, and `false` otherwise. The input `n` is a 32-bit signed integer, and it can be any value between -2^31 and 2^31 - 1.

## Approach
The approach is to use bit manipulation to check if the number is a power of two. A power of two has exactly one bit set to 1 in its binary representation. We can use this property to determine if a number is a power of two.

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
        // edge case: n is less than or equal to 0
        if (n <= 0) return false;
        
        // count the number of bits set to 1
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
- The expression `n & (n - 1)` can be used to count the number of bits set to 1 in the binary representation of `n`.
- The time complexity of this solution is O(1) because it only involves a constant number of operations.