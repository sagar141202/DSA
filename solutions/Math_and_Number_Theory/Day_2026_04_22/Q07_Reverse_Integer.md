# Reverse Integer

## Problem Statement
The problem requires reversing a given 32-bit integer. The integer can be positive or negative. The function should take an integer as input and return the reversed integer. If the reversed integer overflows (i.e., it is outside the range of a 32-bit integer), the function should return 0. For example, the reverse of 123 is 321, and the reverse of -123 is -321.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and then converting it back to an integer. We also need to handle the case where the reversed integer overflows. The sign of the integer is preserved throughout the process.

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
- Use long long to handle potential overflow when reversing the integer.
- Check for overflow after reversing the integer and return 0 if necessary.
- Preserve the sign of the original integer throughout the process.