# Reverse Integer

## Problem Statement
The problem requires reversing a 32-bit signed integer. Given an integer, reverse the digits of the integer while preserving the sign. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), return 0. For example, the reverse of 123 is 321, and the reverse of -456 is -654. The input integer will be in the range [-2^31, 2^31 - 1].

## Approach
The approach involves converting the integer into a string, reversing the string, and then converting it back into an integer while preserving the sign. We also need to check for overflow after reversing the integer.

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
        long long res = 0; // use long long to check for overflow
        int sign = (x < 0) ? -1 : 1;
        x = abs(x);
        while (x > 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        res *= sign;
        if (res < INT_MIN || res > INT_MAX) return 0; // check for overflow
        return (int)res;
    }
};
```

## Test Cases
```
Input: 123
Output: 321
Input: -456
Output: -654
Input: 120
Output: 21
Input: 1534236469
Output: 0
```

## Key Takeaways
- Use long long data type to check for overflow.
- Preserve the sign of the original integer.
- Check for overflow after reversing the integer to ensure it is within the range of a 32-bit signed integer.