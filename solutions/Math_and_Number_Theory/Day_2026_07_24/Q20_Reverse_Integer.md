# Reverse Integer

## Problem Statement
The problem requires writing a function that takes a 32-bit signed integer as input and returns the integer obtained by reversing the order of its digits. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), the function should return 0. The input integer can be positive, negative, or zero. For example, if the input is 123, the output should be 321. If the input is -123, the output should be -321.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and then converting it back to an integer. We also need to handle the case where the reversed integer overflows. The function will check for overflow by comparing the reversed integer with the maximum and minimum 32-bit signed integer values.

## Complexity
- Time: O(log(n))
- Space: O(log(n))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long res = 0; // use long long to handle overflow
        int sign = x < 0 ? -1 : 1;
        x = abs(x);
        while (x > 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        res *= sign;
        // check for overflow
        if (res > INT_MAX || res < INT_MIN) {
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
- Use long long to handle overflow when reversing the integer.
- Check for overflow after reversing the integer.
- Handle negative numbers by storing the sign separately and applying it after reversal.