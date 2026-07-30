# Reverse Integer

## Problem Statement
The problem requires reversing a 32-bit signed integer. Given an integer, reverse the digits of the integer while preserving the sign. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), return 0. The input integer is in the range [-2^31, 2^31 - 1]. For example, the reverse of 123 is 321, and the reverse of -123 is -321.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and converting it back to an integer. We also need to preserve the sign of the original integer and check for overflow.

## Complexity
- Time: O(log|x|)
- Space: O(log|x|)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long res = 0; // Use long long to check for overflow
        int sign = (x < 0) ? -1 : 1; // Preserve the sign
        x = abs(x);
        while (x != 0) {
            res = res * 10 + x % 10; // Reverse the integer
            x /= 10;
        }
        res *= sign; // Restore the sign
        if (res < INT_MIN || res > INT_MAX) { // Check for overflow
            return 0;
        }
        return (int)res;
    }
};
```

## Test Cases
```
Input: 123
Output: 321
Input: -123
Output: -321
Input: 120
Output: 21
Input: 1534236469
Output: 0 (due to overflow)
```

## Key Takeaways
- When dealing with integer reversals, be mindful of potential overflows.
- Converting integers to strings can simplify the reversal process but may not be the most efficient approach.
- Using a long long data type can help detect overflows when reversing integers.