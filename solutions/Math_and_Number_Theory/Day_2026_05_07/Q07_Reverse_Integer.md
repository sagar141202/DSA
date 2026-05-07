# Reverse Integer

## Problem Statement
The problem requires reversing a 32-bit signed integer. Given an integer, reverse the digits of the integer while preserving its sign. The reversed integer should also be a 32-bit signed integer. If the reversed integer overflows, return 0. For example, the reverse of 123 is 321, and the reverse of -456 is -654. The input integer will be in the range [-2^31, 2^31 - 1].

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
        long long res = 0; // use long long to handle overflow
        int sign = (x < 0) ? -1 : 1;
        x = abs(x);
        
        while (x != 0) {
            res = res * 10 + x % 10;
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
Input: 1534236469
Output: 0
```

## Key Takeaways
- We use a long long data type to handle potential overflow when reversing the integer.
- The time complexity is O(log|x|) because we are processing each digit of the input integer once.
- The space complexity is O(log|x|) because in the worst case, we might need to store all the digits of the input integer.