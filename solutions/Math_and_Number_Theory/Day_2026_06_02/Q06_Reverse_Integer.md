# Reverse Integer

## Problem Statement
The problem requires reversing a given 32-bit signed integer. The integer can be positive, negative, or zero. The task is to reverse the digits of the integer while preserving its sign. For example, if the input is 123, the output should be 321. If the input is -456, the output should be -654. The function should handle cases where the reversed integer overflows the 32-bit signed integer range.

## Approach
The approach involves converting the integer to a string, reversing the string, and then converting it back to an integer while preserving the sign. We also need to handle potential overflows by checking if the reversed integer is within the 32-bit signed integer range.

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
        long long res = 0; // using long long to handle potential overflows
        int sign = (x < 0) ? -1 : 1;
        x = abs(x);
        
        while (x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        
        res *= sign;
        
        // checking for overflow
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
Output: 0 (due to overflow)
```

## Key Takeaways
- We use a long long data type to handle potential overflows when reversing the integer.
- We check for overflow after reversing the integer by comparing it with the minimum and maximum values of a 32-bit signed integer.
- The time complexity is O(log|x|) because we are processing each digit of the input integer exactly once.