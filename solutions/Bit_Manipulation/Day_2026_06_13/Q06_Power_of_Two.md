# Power of Two

## Problem Statement
Given an integer `n`, write a function to determine if it is a power of two. A power of two is a number that can be expressed as 2^x, where x is a non-negative integer. The function should return `true` if `n` is a power of two, and `false` otherwise. The input `n` is a 32-bit signed integer, and it can be in the range of -2^31 to 2^31 - 1. For example, the function should return `true` for inputs 1, 2, 4, 8, and `false` for inputs 3, 5, 6.

## Approach
The solution uses bit manipulation to check if a number is a power of two. If a number is a power of two, it has exactly one bit set to 1 in its binary representation. We can use this property to determine if a number is a power of two. We will use the bitwise AND operator to check if a number is a power of two.

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
        if (n <= 0) {
            return false;
        }
        // If n is a power of two, it has exactly one bit set to 1 in its binary representation
        // We can use the bitwise AND operator to check if a number is a power of two
        return (n & (n - 1)) == 0;
    }
};
```

## Test Cases
```
Input: 1
Output: true
Input: 2
Output: true
Input: 3
Output: false
Input: 4
Output: true
Input: 5
Output: false
```

## Key Takeaways
- A power of two has exactly one bit set to 1 in its binary representation.
- The bitwise AND operator can be used to check if a number is a power of two.
- The solution has a time complexity of O(1) and a space complexity of O(1), making it efficient for large inputs.