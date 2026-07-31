# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x, where x is an integer. For example, 1, 2, 4, 8 are powers of two, while 3, 5, 6, 7 are not. The input `n` will be in the range [0, 2^31 - 1]. If `n` is a power of two, the function should return `true`, otherwise `false`.

## Approach
The approach is to use bit manipulation to check if the number is a power of two. A power of two always has exactly one bit set to 1 in its binary representation. We can use this property to determine if a number is a power of two.

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
        
        // a power of two always has exactly one bit set to 1 in its binary representation
        // so, doing a bitwise AND operation with n-1 will give 0 if n is a power of two
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
- A power of two always has exactly one bit set to 1 in its binary representation.
- The bitwise AND operator `&` can be used to check if a number is a power of two.
- The time complexity of the solution is O(1) because it only involves a constant number of operations.