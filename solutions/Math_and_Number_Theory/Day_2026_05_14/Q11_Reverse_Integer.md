# Reverse Integer

## Problem Statement
The problem requires reversing a 32-bit signed integer. Given an integer, reverse the digits of the integer while preserving its sign. The reversed integer should not exceed the 32-bit signed integer range, i.e., it should be between -2^31 and 2^31 - 1. If the reversed integer overflows, return 0. For example, the reverse of 123 is 321, and the reverse of -456 is -654.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and then converting it back to an integer while preserving the sign. We also need to check for overflow after reversing the integer.

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
        long long res = 0; // use long long to detect overflow
        int sign = (x < 0) ? -1 : 1;
        x = abs(x);
        while (x > 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        res *= sign;
        if (res < INT_MIN || res > INT_MAX) { // check for overflow
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
Input: -456
Output: -654
Input: 120
Output: 21
Input: 1534236469
Output: 0
```

## Key Takeaways
- Use long long to detect overflow when reversing the integer.
- Check for overflow after reversing the integer by comparing with INT_MIN and INT_MAX.
- Preserve the sign of the original integer when reversing it.