# Reverse Integer

## Problem Statement
The problem requires reversing a given 32-bit signed integer. The integer can be positive, negative, or zero. The task is to reverse the digits of the integer while preserving its sign. For example, if the input is 123, the output should be 321. If the input is -456, the output should be -654. The reversed integer should also be within the 32-bit signed integer range, i.e., between -2^31 and 2^31 - 1. If the reversed integer overflows, the function should return 0.

## Approach
The algorithm involves converting the integer into a string, separating the sign from the digits, reversing the digits, and then converting the string back into an integer. The sign is preserved throughout the process. The function checks for overflow before returning the reversed integer.

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
        // Initialize variables to store the result and the sign
        long long result = 0;
        int sign = 1;
        
        // Check if the number is negative
        if (x < 0) {
            // Update the sign and convert the number to positive
            sign = -1;
            x = -x;
        }
        
        // Reverse the digits of the number
        while (x != 0) {
            // Extract the last digit of the number
            int digit = x % 10;
            // Append the digit to the result
            result = result * 10 + digit;
            // Remove the last digit from the number
            x = x / 10;
        }
        
        // Restore the sign of the result
        result = sign * result;
        
        // Check for overflow
        if (result < INT_MIN || result > INT_MAX) {
            return 0;
        }
        
        // Return the reversed integer
        return (int)result;
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
Input: 0
Output: 0
```

## Key Takeaways
- The function first checks if the input integer is negative and updates the sign accordingly.
- The digits of the integer are reversed by extracting the last digit and appending it to the result in each iteration.
- The function checks for overflow before returning the reversed integer to ensure it is within the 32-bit signed integer range.