# Reverse Integer

## Problem Statement
The problem requires reversing a 32-bit signed integer. Given an integer, reverse the digits of the integer while preserving the sign. The reversed integer should be within the 32-bit signed integer range, i.e., [-2^31, 2^31 - 1]. If the reversed integer overflows, return 0. For example, the reverse of 123 is 321, and the reverse of -456 is -654.

## Approach
The algorithm involves converting the integer into a string, reversing the string, and then converting it back to an integer. We must handle the sign separately and check for overflow.

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
        
        while (x != 0) {
            int digit = x % 10;
            res = res * 10 + digit;
            x /= 10;
        }
        
        res *= sign;
        
        // check for overflow
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
Input: -456
Output: -654
Input: 120
Output: 21
Input: 1534236469
Output: 0
```

## Key Takeaways
- Always consider edge cases and potential overflows when working with integers.
- Use long long to check for overflow when reversing integers.
- Be mindful of the sign when reversing integers.