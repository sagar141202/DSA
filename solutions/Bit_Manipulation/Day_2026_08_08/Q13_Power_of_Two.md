# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x, where x is a non-negative integer. The function should return `true` if `n` is a power of two, and `false` otherwise. The input `n` will be in the range [0, 2^31 - 1]. For example, the function should return `true` for inputs 1, 2, 4, 8, and `false` for inputs 3, 5, 6.

## Approach
The approach is to use bit manipulation to check if the given number is a power of two. A power of two has exactly one '1' bit in its binary representation. We can use the bitwise AND operator to check this property.

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
        // A power of two has exactly one '1' bit in its binary representation
        // So, doing a bitwise AND operation with n-1 will give us 0
        return n > 0 && (n & (n-1)) == 0;
    }
};
```

## Test Cases
```
Input: 1
Output: true
Input: 3
Output: false
Input: 16
Output: true
```

## Key Takeaways
- A power of two has exactly one '1' bit in its binary representation.
- The bitwise AND operator can be used to check if a number is a power of two.
- This approach has a constant time complexity, making it efficient for large inputs.