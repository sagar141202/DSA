# Reverse Integer

## Problem Statement
The problem requires writing a function that takes a 32-bit signed integer as input and returns the integer obtained by reversing the order of its digits. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), the function should return 0. The input integer can be positive, negative, or zero. For example, if the input is 123, the output should be 321. If the input is -123, the output should be -321.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and then converting it back to an integer. We need to handle the sign of the integer separately and check for overflow.

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
        int sign = (x < 0) ? -1 : 1; // Store the sign of the input integer
        x = abs(x); // Convert the input integer to positive

        while (x > 0) {
            res = res * 10 + x % 10; // Reverse the integer
            x /= 10;
        }

        res *= sign; // Restore the sign of the input integer

        // Check for overflow
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
Input: 1534236469
Output: 0
```

## Key Takeaways
- Use a long long data type to check for overflow when reversing the integer.
- Store the sign of the input integer separately and restore it after reversing the integer.
- Check for overflow after reversing the integer and return 0 if it occurs.