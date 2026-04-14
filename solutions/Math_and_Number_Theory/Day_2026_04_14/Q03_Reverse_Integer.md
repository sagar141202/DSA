# Reverse Integer

## Problem Statement
The problem requires reversing a given 32-bit signed integer. The function should take an integer as input and return the reversed integer. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), the function should return 0. The input integer can be positive, negative, or zero. For example, the reverse of 123 is 321, and the reverse of -456 is -654.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and then converting it back to an integer. We also need to handle the sign of the integer and check for overflow.

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
        int sign = 1;
        if (x < 0) {
            sign = -1;
            x = -x; // make x positive
        }
        while (x > 0) {
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
Input: -456
Output: -654
Input: 120
Output: 21
Input: 1534236469
Output: 0
```

## Key Takeaways
- We use a long long variable to check for overflow.
- We handle the sign of the integer separately to simplify the reversal process.
- The time complexity is O(log|x|) because we are essentially reversing the digits of the integer, and the number of digits is proportional to the logarithm of the absolute value of the integer.