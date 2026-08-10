# Reverse Integer

## Problem Statement
The problem requires reversing a 32-bit signed integer. Given an integer, reverse the digits and return the resulting integer. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), return 0. The input is assumed to be a 32-bit signed integer and the output should also be a 32-bit signed integer. For example, the reverse of 123 is 321, and the reverse of -123 is -321.

## Approach
The algorithm involves converting the integer into a string, reversing the string, and then converting it back into an integer. We also need to check for overflow after reversing the integer.

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
        long long res = 0; // Using long long to check for overflow
        while (x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        // Check for overflow
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
- We use a long long data type to check for overflow after reversing the integer.
- The time complexity is O(log|x|) because we are effectively processing each digit of the input integer once.
- The space complexity is also O(log|x|) because in the worst case, we might need to store all the digits of the input integer.