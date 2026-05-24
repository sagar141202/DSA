# Reverse Integer

## Problem Statement
The problem requires reversing a 32-bit signed integer. Given an integer, reverse the digits of the integer while preserving its sign. For example, if the input is 123, the output should be 321. If the input is -123, the output should be -321. The integer should not overflow during the reversal process. If the reversed integer overflows, return 0.

## Approach
The approach involves converting the integer to a string, reversing the string, and then converting it back to an integer. We also need to handle the sign of the integer separately.

## Complexity
- Time: O(log(x))
- Space: O(log(x))

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long res = 0; // using long long to handle overflow
        int sign = (x < 0) ? -1 : 1;
        x = abs(x);
        while (x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        res *= sign;
        if (res > INT_MAX || res < INT_MIN) {
            return 0; // overflow
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
Input: 0
Output: 0
```

## Key Takeaways
- The time complexity is O(log(x)) because we are processing each digit of the input integer once.
- The space complexity is O(log(x)) because we are storing the reversed integer as a string or in a data structure that can hold up to log(x) digits.
- We use a long long data type to handle overflow during the reversal process.