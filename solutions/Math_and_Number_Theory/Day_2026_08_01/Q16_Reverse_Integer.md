# Reverse Integer

## Problem Statement
The problem requires reversing a given 32-bit signed integer. The integer can be positive, negative, or zero. The reversal should be done in a way that the sign of the integer is preserved. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), the function should return 0. For example, if the input is 123, the output should be 321. If the input is -456, the output should be -654.

## Approach
The algorithm involves converting the integer into a string, reversing the string, and then converting it back into an integer. We need to handle the sign separately to preserve it in the result. The solution also needs to check for integer overflow after reversing.

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
        long long res = 0; // Use long long to check for overflow
        int sign = 1;
        if (x < 0) {
            sign = -1;
            x = -x; // Make x positive for easier calculation
        }
        while (x > 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        res *= sign;
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
Input: -456
Output: -654
Input: 120
Output: 21
Input: 1534236469
Output: 0
```

## Key Takeaways
- Always consider the sign of the integer separately when reversing.
- Use a larger data type (like long long) to check for overflow before casting back to the original type (like int).
- The time complexity is O(log(n)) because the number of digits in an integer n is proportional to log(n).