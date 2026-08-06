# Reverse Integer

## Problem Statement
The problem requires writing a function that takes a 32-bit signed integer as input and returns the integer obtained by reversing the order of its digits. If the reversed integer overflows (i.e., it is outside the range of a 32-bit signed integer), the function should return 0. For example, the reverse of 123 is 321, and the reverse of -456 is -654.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and then converting it back to an integer. It also includes a check for overflow.

## Complexity
- Time: O(log|x|)
- Space: O(log|x|)

## C++ Solution
```cpp
#include <climits>
class Solution {
public:
    int reverse(int x) {
        long long res = 0;
        while (x) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        // check for overflow
        if (res > INT_MAX || res < INT_MIN) {
            return 0;
        }
        return res;
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
- The use of long long to prevent overflow during the reversal process.
- The check for overflow after the reversal to ensure the result is within the 32-bit signed integer range.
- The time complexity is O(log|x|) because we are processing each digit of the input number exactly once.