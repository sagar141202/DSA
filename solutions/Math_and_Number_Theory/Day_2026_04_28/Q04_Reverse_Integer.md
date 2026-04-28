# Reverse Integer

## Problem Statement
The problem requires reversing a given 32-bit signed integer. The integer can be positive, negative, or zero. The task is to reverse the integer while preserving its sign. For example, if the input is 123, the output should be 321. If the input is -456, the output should be -654. The reversed integer should not exceed the 32-bit signed integer range, i.e., it should be between -2^31 and 2^31 - 1. If the reversed integer exceeds this range, the function should return 0.

## Approach
The algorithm involves converting the integer to a string, reversing the string, and then converting it back to an integer. We need to handle the sign separately to preserve it in the result. The integer is reversed by iterating through each digit from the end to the start and appending it to the result.

## Complexity
- Time: O(log|x|) where x is the input integer, because we process each digit of the integer once.
- Space: O(log|x|) because in the worst case, we need to store all digits of the input integer in the reversed string.

## C++ Solution
```cpp
#include <climits>
class Solution {
public:
    int reverse(int x) {
        long long res = 0; // use long long to handle potential overflow
        int sign = 1;
        if (x < 0) {
            sign = -1;
            x = -x; // make x positive for simplicity
        }
        while (x > 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        res *= sign;
        // check if res is within 32-bit signed integer range
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
Output: 0 (because the reversed integer exceeds the 32-bit signed integer range)
```

## Key Takeaways
- Always consider the potential overflow when dealing with integer reversal.
- Handling the sign of the input integer separately simplifies the reversal process.
- Using a long long data type temporarily can help detect potential overflows before converting back to an integer.