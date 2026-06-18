# Reverse Integer

## Problem Statement
The problem requires reversing a 32-bit signed integer. Given an integer, reverse the digits and return the reversed integer. If the reversed integer overflows (is outside the range of a 32-bit signed integer), return 0. For example, the reverse of 123 is 321, and the reverse of -456 is -654. The input integer will be in the range [-2^31, 2^31 - 1].

## Approach
The algorithm involves converting the integer to a string, reversing the string, and converting it back to an integer. It checks for overflow by comparing the reversed integer with the maximum and minimum 32-bit signed integer values.

## Complexity
- Time: O(log|x|)
- Space: O(log|x|)

## C++ Solution
```cpp
#include <climits>
class Solution {
public:
    int reverse(int x) {
        long long res = 0; // using long long to handle overflow
        while (x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
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
Input: -456
Output: -654
Input: 1534236469
Output: 0
```

## Key Takeaways
- Use long long data type to handle potential overflow when reversing the integer.
- Check for overflow after reversing the integer by comparing it with the maximum and minimum 32-bit signed integer values.
- The time complexity is O(log|x|) because the number of digits in an integer is proportional to the logarithm of its absolute value.