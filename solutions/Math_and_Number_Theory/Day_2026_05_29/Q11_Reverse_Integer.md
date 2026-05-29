# Reverse Integer

## Problem Statement
Given a 32-bit signed integer, reverse the digits of the integer while preserving its sign. The reversed integer should also be a 32-bit signed integer. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), return 0. Examples: Input: 123, Output: 321; Input: -123, Output: -321; Input: 120, Output: 21.

## Approach
The approach involves converting the integer to a string, reversing the string, and then converting it back to an integer while preserving the sign. We also need to check for overflow.

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
        long long res = 0;
        int sign = (x < 0) ? -1 : 1;
        x = abs(x);
        while (x) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        res *= sign;
        if (res < INT_MIN || res > INT_MAX) {
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
Output: 0
```

## Key Takeaways
- Check for the sign of the input integer and preserve it in the result.
- Use a long long to handle potential overflow during the reversal process.
- After reversing, check if the result is within the range of a 32-bit signed integer before returning it.